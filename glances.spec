#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : glances
Version  : 2.11
Release  : 21
URL      : https://github.com/nicolargo/glances/archive/v2.11.tar.gz
Source0  : https://github.com/nicolargo/glances/archive/v2.11.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-3.0
Requires: glances-bin
Requires: glances-python3
Requires: glances-license
Requires: glances-man
Requires: glances-python
Requires: psutil
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : psutil
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python-core
BuildRequires : python3-core
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython
BuildRequires : tox
BuildRequires : virtualenv

%description
===============================
Glances - An eye on your system
===============================

%package bin
Summary: bin components for the glances package.
Group: Binaries
Requires: glances-license
Requires: glances-man

%description bin
bin components for the glances package.


%package doc
Summary: doc components for the glances package.
Group: Documentation
Requires: glances-man

%description doc
doc components for the glances package.


%package legacypython
Summary: legacypython components for the glances package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the glances package.


%package license
Summary: license components for the glances package.
Group: Default

%description license
license components for the glances package.


%package man
Summary: man components for the glances package.
Group: Default

%description man
man components for the glances package.


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
export SOURCE_DATE_EPOCH=1530372141
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
export SOURCE_DATE_EPOCH=1530372141
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/glances
cp COPYING %{buildroot}/usr/share/doc/glances/COPYING
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
%defattr(0644,root,root,0755)
%doc /usr/share/doc/glances/*

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/glances/COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/glances.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
