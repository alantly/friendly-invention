# Use a doubly linked list for policy

class LRUCache
  def initialize(capacity)
    @capacity = capacity
    @cache = {}
    @count = 0
    @head = Node.new(nil, nil)
    @tail = Node.new(nil, nil)
    @head.next = @tail
    @tail.prev = @head
  end

  def get(key)
    node = @cache[key]
    if node
      puts "returning #{node}"
      move_to_head(node)
      node.value
    else
      -1
    end
  end

  def move_to_head(node)
    remove_node(node)
    add_node(node)
  end

  def remove_node(node)
    prev = node.prev
    after = node.next
    prev.next = after
    after.prev = prev
    node.next = nil
    node.prev = nil
  end

  def add_node(node)
    @head.next.prev = node
    node.next = @head.next
    @head.next = node
    node.prev = @head
  end

  def remove_last
    if @head.next != @tail
      last = @tail.prev
      remove_node(last)
      last
    end
  end

  def update_node(node, value)
    node.value = value
  end

  def put(key, value)
    if @cache[key]
      @cache[key].value = value
      move_to_head(@cache[key])
    else
      new_node = Node.new(key, value)
      add_node(new_node)
      @cache[key] = new_node
      @count += 1

      if @count > @capacity
        lru = remove_last
        @cache.delete(lru.key)
        @count -= 1
      end
    end
  end
end

class Node
  attr_accessor :next, :prev, :key, :value

  def initialize(key, value)
    @key = key
    @value = value
  end

  def to_s
    "#{key} #{value}"
  end
end

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache.new(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
