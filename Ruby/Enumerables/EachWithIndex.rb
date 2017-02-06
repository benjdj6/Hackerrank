def skip_animals(animals, skip)
    animals.each_with_index.map { |item, index| "#{index}:#{item}" if index >= skip }.compact
end