
%define _major  0
%define _minor  07

Summary:	A very small, fast ADOdb library
Summary(pl):	Bardzo ma³a i szybka biblioteka ADOdb
Name:		adodblite
Version:	%{_major}.%{_minor}
Release:	1
Group:		Libraries
License:	LGPL
Source0:	http://dl.sourceforge.net/adodblite/adodb_lite%{_minor}.tar.gz
# Source0-md5:	c814f47359d0ddd8f9a5d972310cb2ea
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
Microsoft SQL, MySQL, PostgreSQL, SQLite and SyBase.

%description -l pl
ADOdb Lite powsta³a jako efekt zapotrzebowania na ma³y i szybki
zamiennik biblioteki ADOdb na potrzeby gry online nazwanej Alien
Assault Traders. Biblioteka ta oferuje tylko ograniczony zestaw
poleceñ i eliminuje wiêkszo¶æ rzadziej u¿ywanych na stronach WWW
funkcji. Mo¿e z powodzeniem zastêpowaæ ADOdb w sytuacjach, gdy
zaimplementowane funkcje wystarcz± do zachowania funkcjonalno¶ci
strony napisanej z my¶l± o ADOdb. Wymaga mniejszej ilo¶ci pamiêci, a
niejako efektem ubocznym jest znaczne przyspieszenie dzia³ania.

Aktualnie wspierane silniki bazodanowe: Frontbase, Max DB, Mini SQL,
Microsoft SQL, MySQL, PostgreSQL, SQLite oraz SyBase.

%prep
%setup -q -n adodb_lite

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{name}/adodbSQL_drivers/{fbsql,maxdb,msql,mssql{,po},mysql{,i,t},postgres{,64,7},sqlite,sybase}

cp -af *.php *.jpg adodbSQL_drivers \
	$RPM_BUILD_ROOT%{php_pear_dir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{php_pear_dir}/%{name}
