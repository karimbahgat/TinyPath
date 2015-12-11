import pipy
 
packpath = "tinypath.py"
pipy.define_upload(packpath,
                   author="Karim Bahgat",
                   author_email="karim.bahgat.norway@gmail.com",
                   license="MIT",
                   name="tinypath",
                   description="Tinypath is a tiny object-oriented file path module that provides only the most crucial and commonly needed functionality, making it easy to learn and efficient to use.",
                   url="http://github.com/karimbahgat/tinypath",
                   keywords="paths files folders organizing",
                   classifiers=["License :: OSI Approved",
                                "Programming Language :: Python",
                                "Development Status :: 4 - Beta",
                                "Intended Audience :: Developers",
                                "Intended Audience :: Science/Research",
                                'Intended Audience :: End Users/Desktop'],
                   changes=["Lowercased package name"]
                   )

pipy.generate_docs(packpath)
#pipy.upload_test(packpath)
pipy.upload(packpath)

