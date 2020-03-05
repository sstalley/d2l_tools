python3 ./d2l_formatter.py HW3.zip HW3_4
python3 d2l_builder.py ./HW3_4 .c "cc -Wall -Wstrict-prototypes -Wmissing-prototypes -Wshadow -Wconversion -lpthread -lm -lrt" "-o"
python3 d2l_timer.py ./HW3_4 timerargs_3 3
python3 d2l_cat.py ./HW3_4 .tlog .txt .c .clog .outlog .errlog
