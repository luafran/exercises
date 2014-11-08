trap3 ()
{
   echo "Signal SIGQUIT (3) trap"
}

trap15 ()
{
   echo "Signal SIGTERM (15) trap"
}

echo "pid = $$"

trap trap3 3
trap trap15 15


while [ true ]; do
   sleep 1
done

