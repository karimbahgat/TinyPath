import pypi
 
packpath = "ipath.py"
pypi.define_upload(packpath,
                   author="Karim Bahgat",
                   author_email="karim.bahgat.norway@gmail.com",
                   license="MIT",
                   name="iPath",
                   description="Object-oriented file and folder access for day-to-day efficiency.",
                   url="http://github.com/karimbahgat/iPath",
                   keywords="files folders organizing",
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

