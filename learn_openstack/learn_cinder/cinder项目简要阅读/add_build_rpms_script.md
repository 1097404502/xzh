# build.sh
暂时还看不懂。
```bash
#!/bin/sh
MOD_NAME="openstack-cinder-M"
RPMBUILD='/usr/bin/rpmbuild'
RPM_BUILD_DIR=`rpm --eval '%_builddir'`
RPM_BIN_DIR=`rpm --eval '%_rpmdir'`
RPM_SOURCE_DIR=`rpm --eval '%_sourcedir'`
RPM_SPEC_DIR=`rpm --eval '%_specdir'`
VERSION="1.0.0"
RELEASE=`date +%Y%m%d`

#SET ARGS
if [ $# -lt 1 ] ; then
    echo "Usage: $0 branch [release]"
    echo -e "\nNOTE: if release is not given, use current date"
    exit -1
fi

BRANCH=$1

if [[ $2 =~ ^[0-9]+$ ]] ; then
    RELEASE=$2
else
    echo "Usage: $0 branch [release]"
    echo "release :\"$2\", not a valid number."
    exit -1
fi

SCRIPTS="scripts/cinder-dist.conf scripts/cinder.logrotate scripts/cinder-sudoers \
         scripts/cinder-tgt.conf scripts/openstack-cinder-api.service \
         scripts/openstack-cinder-backup.service scripts/openstack-cinder-scheduler.service \
         scripts/openstack-cinder-volume.service"

function make_package(){
    local CURDIR=`pwd`
    mkdir -p $RPM_BUILD_DIR
    mkdir -p $RPM_SOURCE_DIR

    echo ">>>>>>>>> Archive <<<<<<<<<"
    git archive $BRANCH --output="$RPM_BUILD_DIR/$MOD_NAME-$VERSION.tar"
    if [ $? -ne 0 ] ; then
	echo "Archive error"
	exit -2
    fi
    mkdir -p $RPM_BUILD_DIR/$MOD_NAME-$VERSION/
    cp scripts/PKG-INFO $RPM_BUILD_DIR/$MOD_NAME-$VERSION/
    sed -i "s/@@VERSION@@/$VERSION/g" $RPM_BUILD_DIR/$MOD_NAME-$VERSION/PKG-INFO
    cd $RPM_BUILD_DIR

    echo ">>>>>>>>> Extract <<<<<<<<<"
    tar -xf $MOD_NAME-$VERSION.tar -C $MOD_NAME-$VERSION
    rm -f $MOD_NAME-$VERSION.tar

    echo ">>>>>>>>> Make tar <<<<<<<<"
    tar -czf $RPM_SOURCE_DIR/$MOD_NAME-$VERSION.tar.gz $MOD_NAME-$VERSION/

    cd $CURDIR
    for s in $SCRIPTS
    do
        \cp -f $s $RPM_SOURCE_DIR/
    done
    rm -fr $RPM_BUILD_DIR/$MOD_NAME-$VERSION
    rm -f $RPM_BUILD_DIR/$MOD_NAME-$VERSION.tar
}

echo ">>>>>>>> Resolve deps <<<<<<<"
sed -e "s/@@RELEASE@@/$RELEASE/g" \
       -e "s/@@VERSION@@/$VERSION/g" \
       <  $MOD_NAME.spec.in > $MOD_NAME.spec
mkdir -p $RPM_SPEC_DIR
mv $MOD_NAME.spec $RPM_SPEC_DIR/$MOD_NAME.spec

sudo yum-builddep -y $RPM_SPEC_DIR/$MOD_NAME.spec

make_package

echo ">>>>>>>>> RPMS <<<<<<<<"
$RPMBUILD -ba $RPM_SPEC_DIR/$MOD_NAME.spec
[ $? -ne 0 ] && exit -4
rm -fr $RPM_BUILD_DIR/$MOD_NAME-$VERSION

mkdir -p OUTPUT
\cp $RPM_BIN_DIR/noarch/$MOD_NAME-*$VERSION-$RELEASE.noarch.rpm OUTPUT/
\cp $RPM_BIN_DIR/noarch/python-${MOD_NAME/openstack-/}-$VERSION-$RELEASE.noarch.rpm OUTPUT/
\cp $RPM_BIN_DIR/noarch/python-${MOD_NAME/openstack-/}-tests-$VERSION-$RELEASE.noarch.rpm OUTPUT/
ls -l OUTPUT/

```