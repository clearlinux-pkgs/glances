#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : glances
Version  : 2.11
Release  : 9
URL      : https://github.com/nicolargo/glances/archive/v2.11.tar.gz
Source0  : https://github.com/nicolargo/glances/archive/v2.11.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-3.0
Requires: glances-bin
Requires: glances-python3
Requires: glances-doc
Requires: glances-python
Requires: psutil
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : psutil
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv

%description
===============================
Glances - An eye on your system
===============================

%package bin
Summary: bin components for the glances package.
Group: Binaries

%description bin
bin components for the glances package.


%package doc
Summary: doc components for the glances package.
Group: Documentation

%description doc
doc components for the glances package.


%package legacypython
Summary: legacypython components for the glances package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the glances package.


%package python
Summary: python components for the glances package.
Group: Default
Requires: glances-python3

%description python
python components for the glances package.


%package python3
Summary: python3 components for the glances package.
Group: Default
Requires: python3-core

%description python3
python3 components for the glances package.


%prep
%setup -q -n glances-2.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1519395508
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
export SOURCE_DATE_EPOCH=1519395508
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/glances

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/glances/*
%doc /usr/share/man/man1/*

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
