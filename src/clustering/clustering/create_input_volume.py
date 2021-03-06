import nibabel as nb
import numpy as np
import os

from variables import workingdir
import nipype.interfaces.freesurfer as fs
import nipype.interfaces.fsl as fsl
from nipype.utils.filemanip import split_filename

from utils import get_mask

subject_id = '9630905'
workingdir = '/scr/kongo1/NKIMASKS'

preprocessedfile = '/scr/ilz1/Data/results/preprocessed_resting/_session_session1/_subject_id_9630905/_fwhm_0/_bandpass_filter0/afni_corr_rest_roi_dtype_tshift_detrended_regfilt_gms_filt.nii.gz'
regfile = '/scr/ilz1/Data/results/func2anat_transform/_session_session1/_subject_id_9630905/_register0/FREESURFER.mat'

#labels
sourcelabels = [12114, 12113] #ctx_rh_G_front_inf-Triangul, ctx_rh_G_front_inf-Orbital
targetlabels = [11114] #ctx_lh_G_front_inf-Triangul
inputlabels = sourcelabels + targetlabels

#invert transform matrix
invt = fsl.ConvertXFM()
invt.inputs.in_file = regfile
invt.inputs.invert_xfm = True
invt.inputs.out_file = regfile + '_inv.mat'
invt_result= invt.run()

#define source mask (surface, volume)
sourcemask = get_mask(inputlabels)
sourcemaskfile = os.path.join(workingdir,'masks/','sourcemask.nii')
sourceImg = nb.Nifti1Image(sourcemask, None)
nb.save(sourceImg, sourcemaskfile)

#transform anatomical mask to functional space
sourcexfm = fsl.ApplyXfm()
sourcexfm.inputs.in_file = sourcemaskfile
sourcexfm.inputs.in_matrix_file = invt_result.outputs.out_file
_, base, _ = split_filename(sourcemaskfile)
sourcexfm.inputs.out_file = base + '_xfm.nii.gz'
sourcexfm.inputs.reference = preprocessedfile
sourcexfm.inputs.interp = 'nearestneighbour'
sourcexfm.inputs.apply_xfm = True
sourcexfm_result = sourcexfm.run()

#manual source data creation (-mask_source option not yet available in afni)
sourcemask_xfm = nb.load(sourcexfm_result.outputs.out_file).get_data()
inputdata = nb.load(preprocessedfile).get_data()
maskedinput = np.zeros_like(inputdata)
for timepoint in range(inputdata.shape[3]):
    maskedinput[:,:,:,timepoint] = np.where(sourcemask_xfm,inputdata[:,:,:,timepoint],0)
maskedinputfile = os.path.join(workingdir,'masks/','inputfile.nii')
inputImg = nb.Nifti1Image(maskedinput, None)
nb.save(inputImg, maskedinputfile)

##PREPARE TARGET MASK##

#define target mask (surface, volume)
targetlabels = [11114] #ctx_lh_G_front_inf-Triangul
targetmask = get_mask(targetlabels)
targetmaskfile = os.path.join(workingdir, 'masks/', 'targetmask.nii')
targetImg = nb.Nifti1Image(targetmask, None)
nb.save(targetImg, targetmaskfile)

#same transform for target
targetxfm = fsl.ApplyXfm()
targetxfm.inputs.in_file = targetmaskfile
targetxfm.inputs.in_matrix_file = invt_result.outputs.out_file
_, base, _ = split_filename(targetmaskfile)
targetxfm.inputs.out_file = base + '_xfm.nii.gz'
targetxfm.inputs.reference = preprocessedfile
targetxfm.inputs.interp = 'nearestneighbour'
targetxfm.inputs.apply_xfm = True
targetxfm_result = targetxfm.run()
