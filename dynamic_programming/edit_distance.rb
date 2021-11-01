def min_distance(word1, word2)
  chars1 = [""] + word1.split('')
  chars2 = [""] + word2.split('')
  edit_distances = create_initial_edit_distance(chars1, chars2)

  cur_row = 1
  while cur_row < edit_distances.length
    row = edit_distances[cur_row]
    i = 1
    while i < row.length
      if chars1[i] == chars2[cur_row]
        row[i] = edit_distances[cur_row - 1][i - 1]
      else
        row[i] = [row[i-1], edit_distances[cur_row - 1][i - 1],  edit_distances[cur_row - 1][i]].min + 1
      end

      i += 1
    end
    cur_row += 1
  end
  # pretty_print(edit_distances)

  return edit_distances[chars2.length - 1][chars1.length - 1]
end

def create_initial_edit_distance(chars1, chars2)
  edit_distances = []
  chars2.each do |i|
    edit_distances << chars1.map { |k| nil }
  end

  edit_distances[0] = edit_distances[0].map.with_index { |v, i| i }
  edit_distances.each_with_index do |v, i|
    v[0] = i
  end
  return edit_distances
end

def pretty_print(edit_distance)
  edit_distance.each do |ed|
    print ed
    puts
  end
end
