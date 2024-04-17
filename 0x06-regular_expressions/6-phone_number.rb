#!/usr/bin/env ruby

match = ARGV[0].scan(/\A\d{10}\z/)

for a in match
    print a
end
