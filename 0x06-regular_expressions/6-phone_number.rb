#!/usr/bin/env ruby
zenko = ARGV[0]
puts zenko.scan(/^\d{10,10}$/).join
