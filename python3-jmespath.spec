#
# Conditional build:
%bcond_with	tests	# unit tests (incomplete in sdist)

%define		module	jmespath
Summary:	JSON Matching Expressions
Summary(pl.UTF-8):	JSON Matching Expressions - wyrażenia dopasowujące JSON
Name:		python3-%{module}
Version:	1.1.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/jmespath/
Source0:	https://files.pythonhosted.org/packages/source/j/jmespath/%{module}-%{version}.tar.gz
# Source0-md5:	ecc9e47d433b539b7fc87e61972d3746
URL:		https://github.com/jmespath/jmespath.py
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pynose
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.9
Conflicts:	python-jmespath < 0.10.0-9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JMESPath allows you to declaratively specify how to extract elements
from a JSON document.

%description -l pl.UTF-8
JMESPath pozwala deklaratywnie określać sposób wydobywania elementów z
dokumentów JSON.

%prep
%setup -q -n %{module}-%{version}

%{__rm} -r %{module}.egg-info

%build
%py3_build

%if %{with tests}
nosetests-%{py3_ver}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/jp.py $RPM_BUILD_ROOT%{_bindir}/jp.py-3
ln -sf jp.py-3 $RPM_BUILD_ROOT%{_bindir}/jp.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%attr(755,root,root) %{_bindir}/jp.py
%attr(755,root,root) %{_bindir}/jp.py-3
%{py3_sitescriptdir}/jmespath
%{py3_sitescriptdir}/jmespath-%{version}-py%{py3_ver}.egg-info
