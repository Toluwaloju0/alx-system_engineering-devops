#!/usr/bin/env ruby
a = 0
while ARGV[a] != nil
  if ARGV[a].scan(/from/)
      b = ARGV[a].length - 1
      print ARGV[a].slice(5, b)
  elsif ARGV[a].scan(/to/)
      b = ARGV[a].length - 1
      print ARGV[a].slice(3, b)
  elsif ARGV[a].scan(/flags/)
      b = ARGV[a].length - 1
      print ARGV[a].slice(6, b)
  end
  a += 1
end
