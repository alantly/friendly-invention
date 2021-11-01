class TrieNode
  attr_accessor :characters, :end_of_word
  def initialize()
    @characters = {}
    @end_of_word = false
  end
end

class Trie
  def initialize()
    @head = TrieNode.new
  end

  def insert(word)
    _insert(@head, word)
  end

  def _insert(node, word)
    return if word.length == 0

    first_char = word[0]
    remaining_chars = word[1..]

    node.characters[first_char] = TrieNode.new unless node.characters[first_char]
    if remaining_chars.length > 0
      _insert(node.characters[first_char], remaining_chars)
    else
      node.characters[first_char].end_of_word = true
    end
  end

  def search(word)
    _search(node: @head, word: word, prefix_only: false)
  end

  def _search(node:, word:, prefix_only: false)
    return false if word.length == 0

    first_char = word[0]
    remaining_chars = word[1..]

    if node.characters[first_char]
      if remaining_chars.length == 0
        return true if prefix_only
        return node.characters[first_char].end_of_word
      else
        return _search(node: node.characters[first_char], word: remaining_chars, prefix_only: prefix_only)
      end
    else
      return false
    end
  end

  def starts_with(prefix)
    _search(node: @head, word: prefix, prefix_only: true)
  end

  def erase(word)
    _erase(node: @head, word: word)
  end

  def _erase(node:, word:)
    return false if word.length == 0

    first_char = word[0]
    remaining_chars = word[1..]

    if node.characters[first_char]
      char_node = node.characters[first_char]
      if remaining_chars.length == 0 && char_node.end_of_word
        char_node.end_of_word = false
        delete = true
      else
        delete = _erase(node: node.characters[first_char], word: remaining_chars)
      end
      if delete && char_node.characters.size == 0 && !char_node.end_of_word
        node.characters.delete(first_char)
      end
      return delete
    else
      return false
    end
  end
end

require 'minitest/autorun'

describe Trie do
  before do
    @trie = Trie.new
  end

  describe "search" do
    describe "success" do
      it "returns true on stored word" do
        @trie.insert("apple")
        _(@trie.search("apple")).must_equal true
      end

      it "returns true on stored prefix" do
        @trie.insert("apple")
        @trie.insert("app")
        _(@trie.search("app")).must_equal true
      end
    end

    describe "failures" do
      it "returns false on non stored word" do
        _(@trie.search("app")).must_equal false
      end

      it "returns false on non stored prefix" do
        @trie.insert("apple")
        _(@trie.search("app")).must_equal false
      end
    end
  end

  describe "starts_with" do
    describe "success" do
      it "returns true on prefix" do
        @trie.insert("apple")
        _(@trie.starts_with("app")).must_equal true
      end

      it "returns true on word" do
        @trie.insert("apple")
        _(@trie.starts_with("apple")).must_equal true
      end
    end

    describe "failures" do
      it "returns false on when prefix does not exist" do
        _(@trie.starts_with("app")).must_equal false
      end

      it "returns false when prefix does not match" do
        @trie.insert("apple")
        _(@trie.starts_with("apa")).must_equal false
      end
    end
  end

  describe "erase" do
    describe "success" do
      it "returns true on erase" do
        @trie.insert("apple")
        _(@trie.search("apple")).must_equal true

        _(@trie.erase("apple")).must_equal true
        _(@trie.search("apple")).must_equal false
        _(@trie.starts_with("app")).must_equal false
        _(@trie.starts_with("a")).must_equal false
      end
    end

    describe "failures" do
      it "returns false when attempting to delete something that does not exist" do
        _(@trie.erase("app")).must_equal false
      end

      it "returns false when attempting to delete a prefix" do
        @trie.insert("apple")
        _(@trie.erase("app")).must_equal false
      end

      it "returns false when attempting to delete a superset word" do
        @trie.insert("apple")
        _(@trie.erase("apples")).must_equal false
      end
    end
  end
end
