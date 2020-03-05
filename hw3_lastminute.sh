python3 d2l_builder.py ./HW3_LASTMINUTE .c "cc -Wall -Wstrict-prototypes -Wmissing-prototypes -Wshadow -Wconversion -lpthread -lm -lrt" "-o"
python3 d2l_timer.py ./HW3_LASTMINUTE timerargs_3 3
python3 d2l_cat.py ./HW3_LASTMINUTE .tlog .txt .c .clog .outlog .errlog
