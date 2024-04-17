#!/usr/bin/env ruby

match = ARGV[0].scan(/[A-Z]/)

for a in match
    print a
end
