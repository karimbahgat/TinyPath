import pypi
 
packpath = "tinypath.py"
pypi.define_upload(packpath,
                   author="Karim Bahgat",
                   author_email="karim.bahgat.norway@gmail.com",
                   license="MIT",
                   name="TinyPath",
                   description="TinyPath is a tiny object-oriented file path module that provides only the most crucial and commonly needed functionality, making it easy to learn and efficient to use.",
                   url="http://github.com/karimbahgat/TinyPath",
                   keywords="paths files folders organizing",
                   classifiers=["License :: OSI Approved",
                                "Programming Language :: Python",
                                "Development Status :: 4 - Beta",
                                "Intended Audience :: Developers",
                                "Intended Audience :: Science/Research",
                                'Intended Audience :: End Users/Desktop'],
                   )

pypi.generate_docs(packpath)
#pypi.upload_test(packpath)
pypi.upload(packpath)

