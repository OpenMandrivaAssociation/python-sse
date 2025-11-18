Name:		python-sse
Version:	1.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/s/sse/sse-%{version}.tar.gz
Summary:	Server-Sent Events protocol implemetation.
URL:		https://pypi.org/project/sse/
License:	UNKNOWN
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Server-Sent Events protocol implemetation.

%files
%{py_sitedir}/sse.py
%{py_sitedir}/sse-*.*-info
