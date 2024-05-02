for i in 1 2 3 4; do
    kill $(lsof -t -i:800$i)
done