#!/bin/bash

# rails3101.bash

# This script should start a web server to listen on localhost:3101

cd ~/cs101/

bin/rails s -b 0.0.0.0 -p 3101

exit
# I should see something like this:

cs101@ub100:~/cs101 $ bin/rails s -p 3101
=> Booting Puma
=> Rails 5.1.4 application starting in development 
=> Run `rails server -h` for more startup options
[12577] Puma starting in cluster mode...
[12577] * Version 3.11.0 (ruby 2.4.2-p198), codename: Love Song
[12577] * Min threads: 5, max threads: 5
[12577] * Environment: development
[12577] * Process workers: 2
[12577] * Preloading application
[12577] * Listening on tcp://localhost:3101
[12577] Use Ctrl-C to stop
[12577] - Worker 1 (pid: 12615) booted, phase: 0
[12577] - Worker 0 (pid: 12613) booted, phase: 0
