# This is likely a useless program btw

puts "Enter a line that you want to replace all the spaces in:"
line = gets.chomp

puts "What do you want to replace the spaces with?"
line = line.gsub(/\s/, gets.chomp)

puts line
