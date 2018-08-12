import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class GoFish extends CardGame
{
	ArrayList<Rank> playerBooks;
	ArrayList<Rank> computerBooks;
	private Random random;
	
	/**
	 * Constructor for the go fish game. 
	 * This game is played by a player and the computer.
	 * initially 6 cards are drawn. The computer always goes first.
	 * in turn, the player/computer asks for a rank, based on their hand.
	 * If the other player has the rank, then the asker receives all matching cards.
	 * If the other player does not, then the asker draws. If a match is found via the other player or draw, 
	 * then the asking player has another turn. 
	 * the game ends when either player runs out of cards or when the deck is empty.
	 * the object is to create books, or 4 of the same rank in your hand. these are stored at the end of each turn.
	 * the game is scored by he who has the most books. ties are valid.
	 *  @author Brandon Stack
	 */
	public GoFish()
	{
		Title="Go Fish!";
		playerBooks = new ArrayList<Rank>();
		computerBooks = new ArrayList<Rank>();
		random = new Random(System.currentTimeMillis());
	}
	
	/* (non-Javadoc)
	 * @see CardGame#SetRanks()
	 */
	@Override
	protected void SetRanks() 
	{
		ranks.add(Rank.AceLow);
		ranks.add(Rank.two);
		ranks.add(Rank.three);
		ranks.add(Rank.four);
		ranks.add(Rank.five);
		ranks.add(Rank.six);
		ranks.add(Rank.seven);
		ranks.add(Rank.eight);
		ranks.add(Rank.nine);
		ranks.add(Rank.ten);
		ranks.add(Rank.Jack);
		ranks.add(Rank.Queen);
		ranks.add(Rank.King);
	}

	/* (non-Javadoc)
	 * @see CardGame#SetSuits()
	 */
	@Override
	protected void SetSuits() 
	{
		suits.add(Suit.Clubs);
		suits.add(Suit.Diamonds);
		suits.add(Suit.Spades);
		suits.add(Suit.Hearts);
	}


	/* (non-Javadoc)
	 * @see CardGame#GameMenu()
	 */
	@Override
	protected void GameMenu() 
	{//in case the game has setup options
		System.out.println("Start Game - "+Title);
		System.out.println("'x' to exit, when given input prompt.");
	}

	/* (non-Javadoc)
	 * @see CardGame#StartGame()
	 */
	@Override
	protected void StartGame() 
	{
		for(int i=0; i<6; i++)
		{//each player gets 6 cards
			playerHand.addCard(theDeck.draw());
			computerHand.addCard(theDeck.draw());
		}
	}

	/* (non-Javadoc)
	 * @see CardGame#PlayerTurn()
	 */
	@Override
	protected void PlayerTurn() 
	{ 
		System.out.println("\nBegin Player Turn!");
		String input = "";
		Scanner sc = new Scanner(System.in); 
		boolean foundSomething = true;
		while(!input.equals("x") && foundSomething && TestGameEndCondition())
		{
			playerHand.sortHand();
			foundSomething = false; //could have used do-while, chose to do this
			int i = 0;
			System.out.println("Available Cards:");
			for(Card c : playerHand.toList())
			{
				i++;
				System.out.println(i+") "+ c.toString());
			}
			System.out.print("'x' to exit\nSelect: ");
			input=sc.next();
			if(input.equals("x"))
			{
				System.out.println("End Game\n\n");
				Continue=false;
				break;
			}
			try
			{
				
				int value = Integer.parseInt(input);
				Card chosen = playerHand.toList().get(value-1);
				System.out.println("you chose " + chosen.toString());
				for(Card c : computerHand.toList())
				{
					if(c.getRank().ordinal() == chosen.getRank().ordinal())
					{
						foundSomething = true;
						System.out.println("computer has "+ c.toString());
						computerHand.removeCard(c);
						playerHand.addCard(c);
					}
				}
				if(!foundSomething) //we have to fish
				{
					System.out.println("computer says '"+Title+"'");
					System.out.println("You draw a card and... (press any key + enter to draw card)");
					sc.next();//need a little user interaction here
					Card temp =theDeck.draw();
					if(temp.getRank().ordinal()==chosen.getRank().ordinal())
					{
						foundSomething=true;
						System.out.println("Sweet! " + temp.toString());
					}
					else
					{
						System.out.println("Oh, Bad Luck, " + temp.toString());
					}
					playerHand.addCard(temp);
				}
				//search for books
				for(Rank r : ranks)
				{
					if(HasBook(r,playerHand))
					{
						AddBook(r,playerHand,playerBooks);//place books
					}
				}
			}
			catch(Exception e)
			{
				foundSomething=true; //try again
				System.out.println("Error - " + e.getMessage());
			}
		}
		System.out.println("End Player Turn!");
	}

	/* (non-Javadoc)
	 * @see CardGame#ComputerTurn()
	 */
	@Override
	protected void ComputerTurn() 
	{
		/*System.out.println("ComputerHand");//for cheating and testing
		for(Card c : computerHand.toList())
		{
			System.out.println(c.toString());
		}*/
		
		System.out.println("\nBegin Computer Turn!");
		boolean foundSomething = true;
		while(foundSomething && TestGameEndCondition())
		{
			computerHand.sortHand();
			foundSomething = false; //could have used do-while, chose to do this instead
			int a = random.nextInt(computerHand.toList().size());
			Card chosen = computerHand.toList().get(a);
			//the computer is not very bright
			//it will pick the same thing in a row
			//and it will not track your requests
			//I actually like this for keeping the computer easy to play
			System.out.println("The Computer says 'Have any " + chosen.getRank().toString() + "s?'");//no apostrophe
			for(Card c : playerHand.toList())
			{
				if(c.getRank().ordinal() == chosen.getRank().ordinal())
				{
					foundSomething = true;
					System.out.println("Oh no! the computer found your "+ c.toString());
					playerHand.removeCard(c);
					computerHand.addCard(c);
				}
			}
			if(!foundSomething) //we have to fish
			{
				System.out.println("You say '"+Title+"' to the Computer.");
				System.out.println("The Computer Draws and...");
				Card temp =theDeck.draw();
				if(temp.getRank().ordinal()==chosen.getRank().ordinal())
				{
					foundSomething=true;
					System.out.println("Uh oh! " + temp.toString());
				}
				else
				{
					System.out.println("Good luck for you! (computer does not share card)");
				}
				computerHand.addCard(temp);
			}
			//search for books
			for(Rank r : ranks)
			{
				if(HasBook(r,computerHand))
				{
					AddBook(r,computerHand,computerBooks);//place books
				}
			}
		}
		System.out.println("End Computer Turn!");
		
	}

	/* (non-Javadoc)
	 * @see CardGame#TestGameEndCondition()
	 */
	@Override
	protected boolean TestGameEndCondition() 
	{//should we continue?
		return (theDeck.toList().size() > 0 
				&& playerHand.toList().size()>0 
				&& computerHand.toList().size()>0) ;
	}

	/* (non-Javadoc)
	 * @see CardGame#ScoreGame()
	 */
	@Override
	protected void ScoreGame() 
	{
		System.out.println("You had the following Books: ");
		for(Rank r : playerBooks)
		{
			System.out.println(" - " + r);
		}
		System.out.println("The Computer had the following Books: ");
		for(Rank r : computerBooks)
		{
			System.out.println(" - " + r);
		}
		if(playerBooks.size() > computerBooks.size())
		{
			System.out.println("You won!\n\n");
		}
		else if(playerBooks.size() == computerBooks.size())
		{
			System.out.println("You tied the Computer.\n\n");
		}
		else
		{
			System.out.println("The Computer won... :(\n\n");
		}
	}

	/* (non-Javadoc)
	 * @see CardGame#ScoreRank(Rank)
	 */
	@Override
	protected int ScoreRank(Rank rank) 
	{
		return rank.ordinal() + 1;
	}
	/* (non-Javadoc)
	 * @see CardGame#DecisionTurn()
	 */
	@Override
	protected void DecisionTurn() 
	{
		playerHand.sortHand();
		computerHand.sortHand();
		System.out.println("--------------------------END ROUND------------------------------");
		System.out.println("You have "+ playerHand.toList().size() +" cards left");
		System.out.println("The computer has "+ computerHand.toList().size() +" cards left");
		System.out.println("-----------------------------------------------------------------");
	}
	/**
	 * Do we have a book in our hand?
	 *  @author Brandon Stack
	 * @param r
	 * @param hand
	 * @return
	 */
	private boolean HasBook(Rank r, Hand hand)
	{
		int count = 0;
		for(Card c : hand.toList())
		{
			if(c.getRank().ordinal()==r.ordinal()){count++;}
		}
		return count==4;
	}
	/**
	 * Add a book, has to approved before this function is called.
	 *  @author Brandon Stack
	 * @param r
	 * @param hand
	 * @param compendium
	 */
	private void AddBook(Rank r, Hand hand, List<Rank> compendium)
	{
		for(Card c : hand.toList())
		{
			if(c.getRank().ordinal()==r.ordinal())
			{
				hand.removeCard(c);
			}
		}
		compendium.add(r);
	}
	/* (non-Javadoc)
	 * @see CardGame#Reset()
	 */
	@Override
	protected void Reset()
	{
		Continue = true; //for exits from player input
		theDeck = null; //one and only deck, for all games
		playerHand = null;
		computerHand = null;
		playerBooks = new ArrayList<Rank>();
		computerBooks = new ArrayList<Rank>();
	}
}
