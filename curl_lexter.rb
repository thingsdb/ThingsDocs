require 'rouge'
module Rouge
  module Lexers
    class Curl < Rouge::Lexers::Shell
      tag 'curl'
    end
  end
end