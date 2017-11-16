defmodule Hangman do
  def main() do
    pokemon = File.read!("pokemon.txt")
      |> String.split()
      |> Enum.random()
    pokemon = to_charlist(pokemon)
    progress = Enum.map(pokemon, fn x -> "_" end)
   
    gameloop(pokemon, progress, 5)
  end

  def gameloop(pokemon, progress, time) do
    IO.puts progress
    guess = hd(to_charlist(IO.gets "> "))
    matches = Enum.map(pokemon, fn x -> if x == guess, do: x, else: "_" end)
    new_progress = Enum.zip(matches, progress)
      |> Enum.map(fn {x, y} -> Enum.min([x,y]) end)
    cond do
      new_progress == pokemon -> win pokemon
      time <= 0 -> lose pokemon
      Enum.find(pokemon, fn x -> x == guess end) ->
        gameloop(pokemon, new_progress, time)
      true ->
        gameloop(pokemon, new_progress, time - 1)
    end
  end

  def win(pokemon) do
    IO.puts("That's right! It's " <> to_string(pokemon) <> ".")
    IO.puts("Your father and I are so proud of you.")
  end

  def lose(pokemon) do
    IO.puts("You took too long.")
    IO.puts("It was " <> to_string(pokemon) <> " all along.")
  end
end

Hangman.main()
