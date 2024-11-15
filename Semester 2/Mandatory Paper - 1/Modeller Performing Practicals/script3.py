from modeller import *

env = Environ()
aln = Alignment(env)
mdl = Model(env, file='1gz8', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='1gz8A', atom_files='1gz8.pdb')
aln.append(file='qseq.ali', align_codes='qseq')
aln.align2d(max_gap_length=50)
aln.write(file='qseq-1gz8A.ali', alignment_format='PIR')
aln.write(file='qseq-1gz8A.pap', alignment_format='PAP')