python3 ./d2l_formatter.py HW3.zip HW3
python3 d2l_builder.py HW3 .c "cc -Wall -Wstrict-prototypes -Wmissing-prototypes -Wshadow -Wconversion -lpthread -lm -lrt" "-o"
python3 d2l_timer.py HW3 timerargs_3 3
python3 d2l_cat.py ./HW3 .tlog .txt .c .clog .outlog .errlog
