# python3 ./d2l_formatter.py HW2_2.zip HW2_2
python3 d2l_builder.py HW2_Mantha .c "cc -Wall -Wstrict-prototypes -Wmissing-prototypes -Wshadow -Wconversion -lpthread -lm -lrt" "-o"
python3 d2l_timer.py HW2_Mantha timerargs 3
python3 d2l_cat.py ./HW2_Mantha .tlog .txt .c .clog
