#!/usr/bin/env ruby

arg = ARGV[0]

regex = /from:([a-zA-Z0-9+]+)|to:([a-zA-Z0-9+]+)|flags:([0-9:-]+)/

Format = arg.scan(regex)

# The compact method is used here to remove nil values/elements from the array
lists = [Format[0].compact, Format[1].compact, Format[2].compact]

result = lists.join(',')

puts result
