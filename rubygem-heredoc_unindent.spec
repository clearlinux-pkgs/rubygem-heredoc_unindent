#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-heredoc_unindent
Version  : 1.2.0
Release  : 1
URL      : https://rubygems.org/downloads/heredoc_unindent-1.2.0.gem
Source0  : https://rubygems.org/downloads/heredoc_unindent-1.2.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-hoe
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-test-unit

%description
= heredoc_unindent
* https://github.com/adrianomitre/heredoc_unindent
== DESCRIPTION:

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n heredoc_unindent-1.2.0
gem spec %{SOURCE0} -l --ruby > rubygem-heredoc_unindent.gemspec

%build
gem build rubygem-heredoc_unindent.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
heredoc_unindent-1.2.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/heredoc_unindent-1.2.0
ruby -v -I.:lib test*/test_*.rb
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/heredoc_unindent-1.2.0.gem
/usr/lib64/ruby/gems/2.2.0/doc/heredoc_unindent-1.2.0/ri/CoreExt/String/HeredocUnindent/cdesc-HeredocUnindent.ri
/usr/lib64/ruby/gems/2.2.0/doc/heredoc_unindent-1.2.0/ri/CoreExt/String/HeredocUnindent/heredoc_unindent%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/heredoc_unindent-1.2.0/ri/CoreExt/String/HeredocUnindent/heredoc_unindent-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/heredoc_unindent-1.2.0/ri/CoreExt/String/HeredocUnindent/unindent%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/heredoc_unindent-1.2.0/ri/CoreExt/String/HeredocUnindent/unindent-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/heredoc_unindent-1.2.0/ri/CoreExt/String/HeredocUnindent/unindent_base-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/heredoc_unindent-1.2.0/ri/CoreExt/String/HeredocUnindent/unindent_base_new-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/heredoc_unindent-1.2.0/ri/CoreExt/String/HeredocUnindent/unindent_base_old-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/heredoc_unindent-1.2.0/ri/CoreExt/String/cdesc-String.ri
/usr/lib64/ruby/gems/2.2.0/doc/heredoc_unindent-1.2.0/ri/CoreExt/cdesc-CoreExt.ri
/usr/lib64/ruby/gems/2.2.0/doc/heredoc_unindent-1.2.0/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/heredoc_unindent-1.2.0/ri/page-History_rdoc.ri
/usr/lib64/ruby/gems/2.2.0/doc/heredoc_unindent-1.2.0/ri/page-Manifest_txt.ri
/usr/lib64/ruby/gems/2.2.0/doc/heredoc_unindent-1.2.0/ri/page-README_rdoc.ri
/usr/lib64/ruby/gems/2.2.0/gems/heredoc_unindent-1.2.0/.gemtest
/usr/lib64/ruby/gems/2.2.0/gems/heredoc_unindent-1.2.0/History.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/heredoc_unindent-1.2.0/Manifest.txt
/usr/lib64/ruby/gems/2.2.0/gems/heredoc_unindent-1.2.0/README.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/heredoc_unindent-1.2.0/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/heredoc_unindent-1.2.0/lib/heredoc_unindent.rb
/usr/lib64/ruby/gems/2.2.0/gems/heredoc_unindent-1.2.0/test/test_heredoc_unindent.rb
/usr/lib64/ruby/gems/2.2.0/specifications/heredoc_unindent-1.2.0.gemspec
