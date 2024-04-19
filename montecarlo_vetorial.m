counter = 0;
total = str2num(argv(){1});

x = rand(1, total);
y = rand(1, total);
s = (power(x, 2) + power(y, 2)) <= 1;
counter = sum(s);

pi = counter / total * 4;
disp(pi);