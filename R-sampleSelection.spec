%global packname  sampleSelection
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.6_12
Release:          1
Summary:          Sample Selection Models
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-12.tar.gz
Requires:         R-maxLik R-systemfit 
Requires:         R-miscTools 
Requires:         R-VGAM R-MASS R-mvtnorm R-plm 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-maxLik R-systemfit
BuildRequires:    R-miscTools 
BuildRequires:    R-VGAM R-MASS R-mvtnorm R-plm 

%description
Estimation of Sample Selection Models

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help