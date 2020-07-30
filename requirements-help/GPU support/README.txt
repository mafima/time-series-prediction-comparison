GPU support help

Latest Tensorflow documentation about GPU support: https://www.tensorflow.org/install/gpu
help video: https://www.youtube.com/watch?v=qrkEYf-YDyI 


errors i experienced:
	missing path variable CUDA (which is acctually cudnn) in C:tools/cuda
	
solution:
	installing Cudnn to C:tools/cuda and adding it to SYSTEMVARIABLES (see youtube link)



recommended testet setup: (as close as possible)
	windows 10 64bit
	
tested environment install:
	cuda 10.1
	cudNN for cuda10.1 https://developer.nvidia.com/rdp/cudnn-download
	tensorflow 2.1.0
	
	
	
virtual environment (conda):
	(p36gpu) C:\Users\manuel>conda list
	# packages in environment at C:\Users\manuel\Anaconda3\envs\p36gpu:
	#
	# Name                    Version                   Build  Channel
	_pytorch_select           1.1.0                       cpu
	_tflow_select             2.1.0                       gpu
	absl-py                   0.8.1                    py36_0
	asn1crypto                1.3.0                    py36_0
	astor                     0.8.0                    py36_0
	attrs                     19.3.0                     py_0
	backcall                  0.1.0                    py36_0
	blas                      1.0                         mkl
	bleach                    3.1.0                    py36_0
	ca-certificates           2020.1.1                      0
	certifi                   2019.11.28               py36_0
	cffi                      1.14.0           py36h7a1dbc1_0
	chardet                   3.0.4                 py36_1003
	colorama                  0.4.3                      py_0
	cryptography              2.8              py36h7a1dbc1_0
	cudatoolkit               10.0.130                      0
	cudnn                     7.6.5                cuda10.0_0
	cycler                    0.10.0           py36h009560c_0
	decorator                 4.4.1                      py_0
	defusedxml                0.6.0                      py_0
	entrypoints               0.3                      py36_0
	freetype                  2.9.1                ha9979f8_1
	gast                      0.2.2                    py36_0
	google-pasta              0.1.8                      py_0
	grpcio                    1.16.1           py36h351948d_1
	h5py                      2.9.0            py36h5e291fa_0
	hdf5                      1.10.4               h7ebc959_0
	hmmlearn                  0.2.3            py36hc8d92b1_0    conda-forge
	hupper                    1.8.1                    py36_0
	icc_rt                    2019.0.0             h0cc432a_1
	icu                       64.2                 he025d50_1    conda-forge
	idna                      2.8                      py36_0
	importlib_metadata        1.5.0                    py36_0
	intel-openmp              2020.0                      166
	ipykernel                 5.1.4            py36h39e3cac_0
	ipython                   7.12.0           py36h5ca1d4c_0
	ipython_genutils          0.2.0                    py36_0
	jedi                      0.16.0                   py36_0
	jinja2                    2.11.1                     py_0
	joblib                    0.14.1                     py_0
	jpeg                      9c                hfa6e2cd_1001    conda-forge
	jsonschema                3.2.0                    py36_0
	jupyter_client            5.3.4                    py36_0
	jupyter_core              4.6.1                    py36_0
	keras                     2.3.1            py36h21ff451_0    conda-forge
	keras-applications        1.0.8                      py_0
	keras-base                2.3.1                    py36_0
	keras-gpu                 2.3.1                         0
	keras-preprocessing       1.1.0                      py_1
	kiwisolver                1.1.0            py36ha925a31_0
	libblas                   3.8.0                    15_mkl    conda-forge
	libcblas                  3.8.0                    15_mkl    conda-forge
	libclang                  9.0.1           default_hf44288c_0    conda-forge
	libgpuarray               0.7.6                hfa6e2cd_0
	libiconv                  1.15                 h1df5818_7
	liblapack                 3.8.0                    15_mkl    conda-forge
	liblapacke                3.8.0                    15_mkl    conda-forge
	libopencv                 4.2.0                    py36_2    conda-forge
	libpng                    1.6.37               h2a8f88b_0
	libprotobuf               3.11.2               h7bd577a_0
	libpython                 2.1                      py36_0
	libsodium                 1.0.16               h9d3ae62_0
	libtiff                   4.1.0                h56a325e_0
	libwebp                   1.0.2                hfa6e2cd_5    conda-forge
	libxml2                   2.9.9                h464c3ec_0
	libxslt                   1.1.33               h579f668_0
	lxml                      4.5.0            py36h1350720_0
	m2w64-binutils            2.25.1                        5
	m2w64-bzip2               1.0.6                         6
	m2w64-crt-git             5.0.0.4636.2595836               2
	m2w64-gcc                 5.3.0                         6
	m2w64-gcc-ada             5.3.0                         6
	m2w64-gcc-fortran         5.3.0                         6
	m2w64-gcc-libgfortran     5.3.0                         6
	m2w64-gcc-libs            5.3.0                         7
	m2w64-gcc-libs-core       5.3.0                         7
	m2w64-gcc-objc            5.3.0                         6
	m2w64-gmp                 6.1.0                         2
	m2w64-headers-git         5.0.0.4636.c0ad18a               2
	m2w64-isl                 0.16.1                        2
	m2w64-libiconv            1.14                          6
	m2w64-libmangle-git       5.0.0.4509.2e5a9a2               2
	m2w64-libwinpthread-git   5.0.0.4634.697f757               2
	m2w64-make                4.1.2351.a80a8b8               2
	m2w64-mpc                 1.0.3                         3
	m2w64-mpfr                3.1.4                         4
	m2w64-pkg-config          0.29.1                        2
	m2w64-toolchain           5.3.0                         7
	m2w64-tools-git           5.0.0.4592.90b8472               2
	m2w64-windows-default-manifest 6.4                           3
	m2w64-winpthreads-git     5.0.0.4634.697f757               2
	m2w64-zlib                1.2.8                        10
	mako                      1.1.1                      py_0
	markdown                  3.1.1                    py36_0
	markupsafe                1.1.1            py36he774522_0
	matplotlib                3.1.3                    py36_0
	matplotlib-base           3.1.3            py36h64f37c6_0
	mistune                   0.8.4            py36he774522_0
	mkl                       2020.0                      166
	mkl-service               2.3.0            py36hb782905_0
	mkl_fft                   1.0.15           py36h14836fe_0
	mkl_random                1.1.0            py36h675688f_0
	msys2-conda-epoch         20160418                      1
	nbconvert                 5.6.1                    py36_0
	nbformat                  5.0.4                      py_0
	ninja                     1.9.0            py36h74a9793_0
	notebook                  6.0.2                    py36_0
	numpy                     1.18.1           py36h93ca92e_0
	numpy-base                1.18.1           py36hc3f5095_1
	openssl                   1.1.1d               he774522_4
	opt_einsum                3.1.0                      py_0
	pandas                    0.25.3           py36ha925a31_0
	pandas-datareader         0.8.1                      py_0
	pandoc                    2.2.3.2                       0
	pandocfilters             1.4.2                    py36_1
	parso                     0.6.1                      py_0
	pastedeploy               2.0.1                    py36_0
	patsy                     0.5.1                    py36_0
	pickleshare               0.7.5                    py36_0
	pip                       20.0.2                   py36_1
	plaster                   1.0                      py36_1
	plaster_pastedeploy       0.7                      py36_0
	prometheus_client         0.7.1                      py_0
	prompt_toolkit            3.0.3                      py_0
	protobuf                  3.11.2           py36h33f27b4_0
	py-opencv                 4.2.0            py36h5ca1d4c_2    conda-forge
	pycparser                 2.19                     py36_0
	pygments                  2.5.2                      py_0
	pygpu                     0.7.6            py36h452e1ab_0
	pyopenssl                 19.1.0                   py36_0
	pyparsing                 2.4.6                      py_0
	pyqt                      5.12.3           py36h6538335_1    conda-forge
	pyqt5-sip                 4.19.18                  pypi_0    pypi
	pyqtwebengine             5.12.1                   pypi_0    pypi
	pyramid                   1.10.4                   py36_0
	pyreadline                2.1                      py36_1
	pyrsistent                0.15.7           py36he774522_0
	pysocks                   1.7.1                    py36_0
	python                    3.6.9                h5500b2f_0
	python-dateutil           2.8.1                      py_0
	pytorch                   1.3.1           cpu_py36h9f948e0_0
	pytz                      2019.3                     py_0
	pywin32                   227              py36he774522_1
	pywinpty                  0.5.7                    py36_0
	pyyaml                    5.3              py36he774522_0
	pyzmq                     18.1.1           py36ha925a31_0
	qt                        5.12.5               h7ef1ec2_0    conda-forge
	requests                  2.22.0                   py36_1
	scikit-learn              0.21.3           py36h6288b17_0
	scipy                     1.4.1            py36h9439919_0
	send2trash                1.5.0                    py36_0
	setuptools                45.2.0                   py36_0
	six                       1.14.0                   py36_0
	sqlite                    3.31.1               he774522_0
	statsmodels               0.11.0           py36he774522_0
	tensorboard               2.0.0              pyhb38c66f_1
	tensorflow                1.15.0          gpu_py36h2b26d6b_0
	tensorflow-base           1.15.0          gpu_py36h1afeea4_0
	tensorflow-estimator      1.15.1             pyh2649769_0
	tensorflow-gpu            1.15.0               h0d30ee6_0
	termcolor                 1.1.0                    py36_1
	terminado                 0.8.3                    py36_0
	testpath                  0.4.4                      py_0
	theano                    1.0.4                    py36_0
	tornado                   6.0.3            py36he774522_3
	tqdm                      4.40.2                     py_0
	traitlets                 4.3.3                    py36_0
	translationstring         1.3                      py36_1
	urllib3                   1.25.8                   py36_0
	vc                        14.1                 h0510ff6_4
	venusian                  1.2.0                    py36_0
	vs2015_runtime            14.16.27012          hf0eaf9b_1
	wcwidth                   0.1.8                      py_0
	webencodings              0.5.1                    py36_1
	webob                     1.8.5                    py36_0
	werkzeug                  0.14.1                   py36_0
	wheel                     0.34.2                   py36_0
	win_inet_pton             1.1.0                    py36_0
	wincertstore              0.2              py36h7fe50ca_0
	winpty                    0.4.3                         4
	wrapt                     1.11.2           py36he774522_0
	xz                        5.2.4                h2fa13f4_4
	yaml                      0.1.7                hc54c509_2
	zeromq                    4.3.1                h33f27b4_3
	zipp                      2.2.0                      py_0
	zlib                      1.2.11               h62dcd97_3
	zope                      1.0                      py36_1
	zope.deprecation          4.4.0                    py36_0
	zope.interface            4.7.1            py36he774522_0
	zstd                      1.3.7                h508b16e_0
