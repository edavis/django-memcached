from setuptools import setup, find_packages

setup(
    name                 = 'django-memcached2',
    version              = '0.1',
    description          = 'django-memcached2 displays statistics about your currently running memcached instances',
    long_description     = open('README.rst').read(),
    keywords             = 'memcached, django, caching, caches',
    author               = 'Eric Davis',
    author_email         = 'ed@npri.org',
    url                  = 'http://github.com/edavis/django-memcached',
    license              = 'BSD',
    packages             = find_packages(),
    zip_safe             = False,
    install_requires     = ['setuptools'],
    include_package_data = True,
    setup_requires       = ['setuptools_git'],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Monitoring",
    ],
)
