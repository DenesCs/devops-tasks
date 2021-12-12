#!/bin/sh

set -e

YAMLS=$(ls nginx-http-server/*.yaml)
eval "
cat <<EOF
$(sed 's/#\$/$/' $YAMLS)
EOF" | kubectl apply -f -

