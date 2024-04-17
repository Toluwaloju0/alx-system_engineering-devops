#!/usr/bin/env ruby

match = ARGV[0].scan(/hbt{2,5}n/)

for a in match
    print a
end
