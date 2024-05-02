for i in 1 2 3 4; do
    echo "python3 node 800$i node$i"
    python3 node 800$i node$i &
done