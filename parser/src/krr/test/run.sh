# ---------------------------------------------------------------------
#   Tested with Java 8
# ---------------------------------------------------------------------

echo `date +%Y-%m-%d:%H:%M:%S.%N` "begin"

JARDIR="../../.."
JARS="$JARDIR/dist/KRR.jar;$JARDIR/lib/antlr-3.5.2-runtime.jar"

java -cp $JARS krr.main.Tool -MAN   input/output.txt  1>output/output.xml

echo `date +%Y-%m-%d:%H:%M:%S.%N` "end"
