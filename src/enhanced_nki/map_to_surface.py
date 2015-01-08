import nipype.pipeline.engine as pe
import nipype.interfaces.utility as util
import nipype.interfaces.io as nio
from nipype.interfaces.freesurfer import SampleToSurface 



subjects = ['0152992',
 '0189478',
 '0154555',
 '0196198',
 '0108355',
 '0120652',
 '0133436',
 '0173085',
 '0103525',
 '0125762',
 '0183277',
 '0168357',
 '0111282',
 '0153460',
 '0182795',
 '0149662',
 '0178174',
 '0169007',
 '0130424',
 '0142609',
 '0152968',
 '0106057',
 '0177681',
 '0166210',
 '0116842',
 '0119486',
 '0131832',
 '0137073',
 '0187473',
 '0197836',
 '0150880',
 '0111693',
 '0156730',
 '0197456',
 '0169571',
 '0119351',
 '0153754',
 '0114232',
 '0122816',
 '0141860',
 '0164385',
 '0137679',
 '0162704',
 '0142673',
 '0142579',
 '0143391',
 '0102019',
 '0182376',
 '0122512',
 '0117168',
 '0180093',
 '0179873',
 '0139212',
 '0129348',
 '0121437',
 '0121400',
 '0166094',
 '0125107',
 '0123429',
 '0181535',
 '0116065',
 '0114446',
 '0164326',
 '0100451',
 '0150404',
 '0103714',
 '0127665',
 '0116041',
 '0120486',
 '0133646',
 '0191053',
 '0156928',
 '0123657',
 '0137714',
 '0120538',
 '0155419',
 '0114139',
 '0192736',
 '0189418',
 '0130249',
 '0151876',
 '0158744',
 '0161513',
 '0138558',
 '0115454',
 '0182604',
 '0105521',
 '0153790',
 '0110559',
 '0173286',
 '0135671',
 '0134715',
 '0127800',
 '0138497',
 '0142513',
 '0157947',
 '0176753',
 '0118439',
 '0188939',
 '0128159',
 '0168013',
 '0136416',
 '0151580',
 '0123173',
 '0195031',
 '0171510',
 '0113013',
 '0109727',
 '0143867',
 '0108184',
 '0105922',
 '0160620',
 '0114275',
 '0103872',
 '0173358',
 '0196651',
 '0181960',
 '0187635',
 '0149794',
 '0109819',
 '0178453',
 '0110184',
 '0196558',
 '0163228',
 '0164900',
 '0167693',
 '0120493',
 '0174363',
 '0186697',
 '0170750',
 '0106459',
 '0194023',
 '0199620',
 '0176479',
 '0170636',
 '0117747',
 '0190053',
 '0193222',
 '0118051',
 '0132717',
 '0126369',
 '0168239',
 '0101783',
 '0137496',
 '0116415',
 '0113044',
 '0133894',
 '0194108',
 '0185676',
 '0105290',
 '0139437',
 '0181439',
 '0192197',
 '0120859',
 '0122169',
 '0108829',
 '0148071',
 '0189280',
 '0185428',
 '0179309',
 '0103384',
 '0154419',
 '0156263',
 '0159429',
 '0145411',
 '0195236',
 '0131637',
 '0166009',
 '0108781',
 '0126919',
 '0115824',
 '0144314',
 '0156678',
 '0114047',
 '0168413',
 '0188854',
 '0143484',
 '0109459',
 '0157580',
 '0150062',
 '0112249',
 '0130678',
 '0179283',
 '0116039',
 '0154423',
 '0108886',
 '0165660',
 '0150589',
 '0152384',
 '0187884',
 '0185781',
 '0141473',
 '0139480',
 '0158411',
 '0165532',
 '0163508',
 '0117902',
 '0188976',
 '0171391',
 '0177857',
 '0186277',
 '0119866',
 '0164993',
 '0105488',
 '0127784',
 '0157873',
 '0161200',
 '0167827',
 '0163059',
 '0106780',
 '0198357',
 '0188219',
 '0103347',
 '0114008',
 '0178964',
 '0132049',
 '0115321',
 '0166987',
 '0171266',
 '0173496',
 '0144544',
 '0146714',
 '0194956',
 '0139077',
 '0180308',
 '0160872',
 '0155458',
 '0105356',
 '0141795',
 '0188199',
 '0123116',
 '0162902',
 '0103645',
 '0175411',
 '0155568',
 '0175151',
 '0160099',
 '0147122',
 '0120818',
 '0158560',
 '0117124',
 '0115684',
 '0123048',
 '0186067',
 '0144495',
 '0169847',
 '0177059',
 '0136018',
 '0122844',
 '0120557',
 '0127484',
 '0176913',
 '0168007',
 '0124028',
 '0155677',
 '0132088',
 '0174886',
 '0152872',
 '0117964',
 '0104892',
 '0124714',
 '0166731',
 '0134505',
 '0101463',
 '0127468',
 '0139300',
 '0198130',
 '0112536',
 '0144702',
 '0162251',
 '0152189',
 '0139764',
 '0161530',
 '0179005',
 '0150525',
 '0131127',
 '0168489',
 '0153114',
 '0199340',
 '0134795',
 '0172228',
 '0115564',
 '0177330',
 '0135591',
 '0112828',
 '0116834',
 '0158726',
 '0198051',
 '0199155',
 '0113030',
 '0184446',
 '0117289',
 '0183457',
 '0190501',
 '0102157',
 '0136649',
 '0112347',
 '0176211',
 '0113436',
 '0153131',
 '0192604',
 '0181315',
 '0167628',
 '0144667',
 '0150716',
 '0190475',
 '0198985',
 '0132995',
 '0127733',
 '0164093',
 '0183726',
 '0132850',
 '0170363',
 '0193358',
 '0146865',
 '0136303',
 '0123971',
 '0196445',
 '0179454']

nki_dicom_dir = "/scr/kalifornien1/data/nki_enhanced/dicoms"
#brain_database_dir = '/scr/adenauer1/dicoms/'
workingdir = "/scr/kansas1/workingdir/nki"

nki_preprocessed_dir = "/scr/kalifornien1/data/nki_enhanced/preprocessed_fmri"

if __name__ == '__main__':
    wf = pe.Workflow(name="map_to_urface")
    wf.base_dir = workingdir
    wf.config['execution']['crashdump_dir'] = wf.base_dir + "/crash_files"
    
    subjects_infosource = pe.Node(util.IdentityInterface(fields=['subject_id']), name="subject_infosource")
    subjects_infosource.iterables = ('subject_id', subjects)
    
    trs_infosource = pe.Node(util.IdentityInterface(fields=['tr']), name="trs_infosource")
    trs_infosource.iterables = ('tr', ['645', '1400', '2500'])
    
    templates_infosource = pe.Node(util.IdentityInterface(fields=['template_name']), name="templates_infosource")
    templates_infosource.iterables = ('template_name', ['fsaverage3', 'fsaverage4', 'fsaverage5'])
    
    hemi_infosource = pe.Node(util.IdentityInterface(fields=['hemi']), name="hemi_infosource")
    hemi_infosource.iterables = ('hemi', ['lh', 'rh'])
    
    datagrabber = pe.Node(nio.DataGrabber(infields=['tr', 'subject_id'], outfields=['preprocessed_resting', 'reg_file']), 
                          name="datagrabber")
    datagrabber.inputs.base_directory = nki_preprocessed_dir
    datagrabber.inputs.template = 'results%s/%s/preproc/%s'
    datagrabber.inputs.template_args['preprocessed_resting'] = [['tr', 'subject_id', 'output/bandpassed/fwhm_0.0/*_afni_bandpassed.nii.gz']]
    datagrabber.inputs.template_args['reg_file'] = [['tr', 'subject_id', 'bbreg/*.dat']]
    datagrabber.inputs.sort_filelist = True
    datagrabber.inputs.raise_on_empty = False

    wf.connect(subjects_infosource, "subject_id", datagrabber, "subject_id")
    wf.connect(trs_infosource, "tr", datagrabber, "tr")
    
    def gen_out_file(tr, template_name, hemi, subject_id):
        from distutils.dir_util import mkpath
        path = "/scr/kalifornien1/data/nki_enhanced/preprocessed_fmri/results%s/%s/preproc/output/bandpassed/fwhm_6.0/"%(tr, subject_id)
        mkpath(path)
        return path + "RsfMRI_preprocessed_%s_%s.%s.nii.gz"%(subject_id, template_name, hemi)
    
    new_name = pe.Node(util.Function(input_names=['tr', 'template_name', 'hemi', 'subject_id'], output_names=['name'], function=gen_out_file), name="new_name")
    wf.connect(subjects_infosource, "subject_id", new_name, "subject_id")
    wf.connect(trs_infosource, "tr", new_name, "tr")
    wf.connect(templates_infosource, "template_name", new_name, "template_name")
    wf.connect(hemi_infosource, "hemi", new_name, "hemi")
    
    vol2surf = pe.Node(SampleToSurface(), name="vol2surf")
    vol2surf.inputs.subjects_dir = '/scr/kalifornien1/data/nki_enhanced/freesurfer'
    vol2surf.inputs.interp_method = "trilinear"
    vol2surf.inputs.cortex_mask = True
    vol2surf.inputs.sampling_method = "average"
    vol2surf.inputs.sampling_range = (0.2, 0.8, 0.1)
    vol2surf.inputs.sampling_units = "frac"
    vol2surf.inputs.smooth_surf = 6.0
    
    wf.connect(datagrabber, 'preprocessed_resting', vol2surf, 'source_file')
    wf.connect(datagrabber, 'reg_file', vol2surf, 'reg_file')
    wf.connect(hemi_infosource, 'hemi', vol2surf, 'hemi')
    wf.connect(templates_infosource, 'template_name', vol2surf, 'target_subject')
    wf.connect(new_name, 'name', vol2surf, 'out_file')
    
    wf.run(plugin="CondorDAGMan")
                          
                          
    
