#!/usr/bin/env ruby

match = ARGV[0].scan(/h[1-9a-zA-Z]n/)

for a in match
    print a
end
