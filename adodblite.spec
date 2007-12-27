
%bcond_with	tests		# build with tests
%bcond_without	doc	# build without documentation

%define _major  1
%define _minor  42

Summary:	A very small, fast ADOdb library
Summary(pl.UTF-8):	Bardzo mała i szybka biblioteka ADOdb
Name:		adodblite
Version:	%{_major}.%{_minor}
Release:	0.1
Group:		Libraries
License:	LGPL
Source0:	http://dl.sourceforge.net/adodblite/adodb_lite%{_major}.%{_minor}.tar.gz
# Source0-md5:	c85b343c34a3e34de4a54b0dd046e338
URL:		http://adodblite.sourceforge.net/
Requires:	php-pear >= 4.0.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		php_pear_dir	%{_datadir}/pear

%description
ADOdb Lite was a result of a need for a very small, fast ADOdb library
for a browser based game called Alien Assault Traders. This library
has a very restricted command set and eliminates most of the esoteric
commands that will not be used by most websites. ADOdb Lite is a drop
in replacement for ADOdb as long as you are not using unsupported
commands on your website. It gives you a smaller memory footprint and,
as a side benefit, greatly improves speed.

It currently supports the following DBMS: Frontbase, Max DB, Mini SQL,
MSSQL, MSSQL Pro, MySQLi, MySQLt, MySQL, PostgreSQL, PostgreSQL64,
PostgreSQL7, PostgreSQL8, SQLite, SQLite Pro, Sybase and Sybase ASE.

%description -l pl.UTF-8
ADOdb Lite powstała jako efekt zapotrzebowania na mały i szybki
zamiennik biblioteki ADOdb na potrzeby gry online nazwanej Alien
Assault Traders. Biblioteka ta oferuje tylko ograniczony zestaw
poleceń i eliminuje większość rzadziej używanych na stronach WWW
funkcji. Może z powodzeniem zastępować ADOdb w sytuacjach, gdy
zaimplementowane funkcje wystarczą do zachowania funkcjonalności
strony napisanej z myślą o ADOdb. Wymaga mniejszej ilości pamięci, a
niejako efektem ubocznym jest znaczne przyspieszenie działania.

Aktualnie wspierane silniki bazodanowe: Frontbase, Max DB, Mini SQL,
MSSQL, MSSQL Pro, MySQLi, MySQLt, MySQL, PostgreSQL, PostgreSQL64,
PostgreSQL7, PostgreSQL8, SQLite, SQLite Pro, Sybase oraz Sybase ASE.

%prep
%setup -q -n adodb_lite

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{name}/adodbSQL_drivers/{fbsql,maxdb,msql,mssql{,po},mysql{,i,t},postgres{,64,7,8},sqlite{,po},sybase{,_ase}}

cp -af *.php adodbSQL_drivers generic_modules session \
	$RPM_BUILD_ROOT%{php_pear_dir}/%{name}

%if %{with doc}
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}
cp -af documentation/* $RPM_BUILD_ROOT%{_docdir}/%{name}
%endif

%if %{with tests}
cp -af tests $RPM_BUILD_ROOT%{php_pear_dir}/%{name}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{name}
%if %{with doc}
%{_docdir}/%{name}
%endif
