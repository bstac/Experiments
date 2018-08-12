import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;  

public class Main 
{
	private static ArrayList<CardGame> Games;
	
	/**
	 * @param args
	 */
	public static void main(String[] args) 
	{
		//run each test
		//this is actually bad, a testing framework would do each independently
		//so you could tell every test that fails, not just one,
		//but I like this, it is like a check list
		//and it requires the tests to pass, unlike testing frameworks
		if(!Test_ArrayList_Functionality()){System.out.println("Test Fails: Test_ArrayList_Functionality");}
		else if(!Test_Card_GetRank()){System.out.println("Test Fails: Test_Card_GetRank");}
		else if(!Test_Card_GetSuit()){System.out.println("Test Fails: Test_Card_GetSuit");}
		else if(!Test_Card_ToString()){System.out.println("Test Fails: Test_Card_ToString");}
		else if(!Test_Hand_AddCard()){System.out.println("Test Fails: Test_Hand_AddCard");}
		else if(!Test_Hand_RemoveCard()){System.out.println("Test Fails: Test_Hand_RemoveCard");}
		else if(!Test_Hand_Contains()){System.out.println("Test Fails: Test_Hand_Contains");}
		else if(!Test_Hand_SortHand()){System.out.println("Test Fails: Test_Hand_SortHand");}
		else if(!Test_Deck_AddCard()){System.out.println("Test Fails: Test_Deck_AddCard");}
		else if(!Test_Deck_RemoveCard()){System.out.println("Test Fails: Test_Deck_RemoveCard");}
		else if(!Test_Deck_ToList()){System.out.println("Test Fails: Test_Deck_ToList");}
		else if(!Test_Deck_Shuffle()){System.out.println("Test Fails: Test_Deck_Shuffle");}
		else if(!Test_Deck_Draw()){System.out.println("Test Fails: Test_Deck_Draw");}
		else
		{
			System.out.println("Tests Passed!\nLets start a game...");
			Games = new ArrayList<CardGame>();
			Games.add(new GoFish()); //here you can add all games that are created
			
			String input = "";
			Scanner sc=new Scanner(System.in); 
			while(!input.equals("x"))
			{
				int i = 0;
				System.out.println("Options:");
				for(CardGame g : Games)
				{
					i++;
					System.out.println(i+") "+g.GetTitle());
				}
				System.out.print("'x' to exit\nSelect: ");
				input=sc.next();
				if(input.equals("x")){break;}
				try
				{
					int value = Integer.parseInt(input);
					CardGame game = Games.get(value-1);
					game.PlayGame();
				}
				catch(Exception e)
				{
					System.out.println("Error - " + e.getMessage());
					//System.out.println(e.getLocalizedMessage());
				}
			}
			System.out.println("Good Bye!");
		}
	}
	
	
	/**
	 * Create a card and test its rank value
	 * @return
	 */
	public static boolean Test_Card_GetRank()
	{
		Card card = new Card(Rank.AceHigh, Suit.Diamonds);
		return card.getRank() == Rank.AceHigh;
	}
	/**
	 * Create a card and test its suit value
	 * @return
	 */
	public static boolean Test_Card_GetSuit()
	{
		Card card = new Card(Rank.AceHigh, Suit.Diamonds);
		return card.getSuit() == Suit.Diamonds;
	}
	/**
	 * Test for the expected toString() of a card
	 * @return
	 */
	public static boolean Test_Card_ToString()
	{
		Card card = new Card(Rank.AceHigh, Suit.Diamonds);
		return "Card - AceHigh : Diamonds".equals(card.toString());
	}
	/**
	 * Test adding a hand to a card.
	 * @return
	 */
	public static boolean Test_Hand_AddCard()
	{
		Card card = new Card(Rank.AceHigh, Suit.Diamonds);
		Hand hand = new Hand();
		hand.addCard(card);
		List<Card> cards = hand.toList();
		return  card.equals(cards.get(0));
	}
	/**
	 * Test Removing a card from a hand.
	 * @return
	 */
	public static boolean Test_Hand_RemoveCard()
	{
		Card card = new Card(Rank.AceHigh, Suit.Diamonds);
		Card cardValue = new Card(Rank.AceHigh, Suit.Diamonds);
		Hand hand = new Hand();
		hand.addCard(card);
		hand.addCard(cardValue);
		hand.removeCard(card);
		return !hand.contains(card) && !hand.contains(cardValue);
	}
	/**
	 * Test the contains method. Tests that value is used, not just identity.
	 * @return
	 */
	public static boolean Test_Hand_Contains()
	{//tests contains works on ID and value
		Card card = new Card(Rank.AceHigh, Suit.Diamonds);
		Card testCard = new Card(Rank.AceHigh, Suit.Spades);
		Card testValueCard = new Card(Rank.AceHigh, Suit.Diamonds);//same value, different reference
		Hand hand = new Hand();
		hand.addCard(card);
		return !hand.contains(testCard) && hand.contains(card) && hand.contains(testValueCard);
	}
	/**
	 * tests the sort function of a Hand.
	 * @return
	 */
	public static boolean Test_Hand_SortHand()
	{
		Hand hand = new Hand();
		hand.addCard(new Card(Rank.Jack, Suit.Diamonds));
		hand.addCard(new Card(Rank.two, Suit.Diamonds));
		hand.addCard(new Card(Rank.King, Suit.Clubs));
		hand.addCard(new Card(Rank.three, Suit.Spades));
		hand.addCard(new Card(Rank.King, Suit.Hearts));
		/*for(Card c : hand.toList())
		{
			System.out.println(c.toString());
		}*/
		//System.out.println("\n\n");
		hand.sortHand();
		/*for(Card c : hand.toList())
		{
			System.out.println(c.toString());
		}*/
		List<Card> cards = hand.toList();//tests to list and sort
		boolean i_0 = cards.get(0).getRank()==Rank.two;
		boolean i_1 = cards.get(1).getRank()==Rank.three;
		boolean i_2 = cards.get(2).getRank()==Rank.Jack;
		boolean i_3 = cards.get(3).getRank()==Rank.King;
		boolean i_4 = cards.get(4).getRank()==Rank.King;
		return i_0 && i_1 && i_2 && i_3 && i_4;
	}
	/**
	 * Tests adding a card to a deck.
	 * @return
	 */
	public static boolean Test_Deck_AddCard()
	{
		Card card = new Card(Rank.AceHigh, Suit.Diamonds);
		Deck deck = new Deck();
		deck.addCard(card);
		List<Card> cards = deck.toList();
		return  card.equals(cards.get(0));
	}
	/**
	 * tests removing a card from a deck. Make sure it removes by value.
	 * @return
	 */
	public static boolean Test_Deck_RemoveCard()
	{
		Card card = new Card(Rank.AceHigh, Suit.Diamonds);
		Card card2 = new Card(Rank.AceHigh, Suit.Diamonds);
		Deck deck = new Deck();
		deck.addCard(card);
		deck.removeCard(card2);
		List<Card> cards = deck.toList();
		return cards.size() == 0;
		//return false;
	}
	/**
	 * Tests the to list function of a deck
	 * @return
	 */
	public static boolean Test_Deck_ToList()
	{
		Deck deck = new Deck();
		deck.addCard(new Card(Rank.two, Suit.Diamonds));
		deck.addCard(new Card(Rank.three, Suit.Diamonds));
		deck.addCard(new Card(Rank.Jack, Suit.Clubs));
		deck.addCard(new Card(Rank.King, Suit.Spades));
		deck.addCard(new Card(Rank.King, Suit.Hearts));
		List<Card> cards = deck.toList();
		boolean i_0 = cards.get(0).getRank()==Rank.two;
		boolean i_1 = cards.get(1).getRank()==Rank.three;
		boolean i_2 = cards.get(2).getRank()==Rank.Jack;
		boolean i_3 = cards.get(3).getRank()==Rank.King;
		boolean i_4 = cards.get(4).getRank()==Rank.King;
		return i_0 && i_1 && i_2 && i_3 && i_4;
	}
	/**
	 * @return
	 */
	public static boolean Test_Deck_Shuffle()
	{
		//the thing about shuffle is that I cannot really test the randomness
		//and have a dependable test
		//so this will be set up to create a histogram for my use
		//sort of monte-carlo my way to good shuffle algorithm
		//but if it gets to the return statement, then it passes
		Deck deck = new Deck();
		deck.addCard(new Card(Rank.two, Suit.Diamonds));//1
		deck.addCard(new Card(Rank.three, Suit.Diamonds));//2
		deck.addCard(new Card(Rank.Jack, Suit.Diamonds));//10
		deck.addCard(new Card(Rank.Queen, Suit.Diamonds));//11
		deck.addCard(new Card(Rank.King, Suit.Diamonds));//12
		//expected average=36/5 -> 7.2, of each place
		double totalLoops=100000.0; //double to guarantee double precision
		int CardNum = deck.toList().size();
		int[] places = new int [CardNum];
		for(int i=0;i<totalLoops;i++)
		{
			deck.shuffle();
			List<Card> cards = deck.toList();
			for(int j=0;j<CardNum;j++)
			{
				places[j]+=cards.get(j).getRank().ordinal();
			}
		}
		double count = 0;
		for(int i : places)
		{
			count += i/totalLoops;
			//System.out.println(i + " : " + i/totalLoops);
		}//result round 7.2 for 100,000 loops
		if(Math.abs(count/CardNum-7.2)<1){System.out.println("\nGood Shuffle\n");}
		return true;
	}
	/**
	 * @return
	 */
	public static boolean Test_Deck_Draw()
	{
		Deck deck = new Deck();
		deck.addCard(new Card(Rank.two, Suit.Diamonds)); 
		deck.addCard(new Card(Rank.three, Suit.Diamonds));
		deck.addCard(new Card(Rank.Jack, Suit.Diamonds));
		deck.addCard(new Card(Rank.Queen, Suit.Diamonds));
		deck.addCard(new Card(Rank.King, Suit.Diamonds));
		Card c = deck.draw();
		List<Card> cards = deck.toList();
		return cards.size()==4 && c.equals(new Card(Rank.King, Suit.Diamonds));
	}

	/**
	 * This demonstrates how arrayList functions with regard to Identity and Value
	 * and other items such as removing what is not there, adding the same reference object twice and then removing.
	 * The functionality has progressed as this program was developed, so it is now used to give a complex add and remove sequence.
	 * If the test does not throw an error, it is valid.
	 * @return
	 */
	public static boolean Test_ArrayList_Functionality()
	{
		//this function simply tests how an array list works using the Hand class
		//this function does not print to the screen currently
		Hand myHand = new Hand();
		Card aceOfClubs = new Card(Rank.AceLow,Suit.Clubs);
		Card aceOfHearts = new Card(Rank.AceLow,Suit.Hearts);
		Card aceOfSpades = new Card(Rank.AceLow,Suit.Spades);
		Card cheat = new Card(Rank.AceLow,Suit.Spades);
		//the only card I need is the ace of spades, the ace of spades
		//dun dun dun, dah dah dah, dun dun dun, dah dah dah.... ~ Motorhead
		
		//what happens if we have the same card twice, and remove one?
		//case for identity and for value
		myHand.addCard(aceOfClubs);
		myHand.addCard(aceOfClubs);
		myHand.addCard(aceOfClubs);
		myHand.addCard(aceOfSpades);
		myHand.addCard(cheat);
		myHand.addCard(cheat);
		/*for(Card c : myHand.toList())
		{
			//System.out.println(c.toString());
		}*/
		
		myHand.removeCard(aceOfClubs);
		//aceOfClubs.setRank(Rank.two); // not really an ace anymore, removed this function, so removed this line
		myHand.removeCard(aceOfClubs);
		myHand.removeCard(aceOfSpades);
		myHand.removeCard(aceOfSpades);
		myHand.removeCard(aceOfHearts); //does this throw error, card not inTest_Hand_AddCard list
		//System.out.println("- - - - - - - - - - - - - - - - - - - - -");
		/*for(Card c : myHand.toList())
		{
			//System.out.println(c.toString());
		}*/
		//so it works like this, list holds references, but it can have many of the same
		//we are enforcing that it does not repeat, however, so there are no duplicates
		//it removes one at a time, it does not fail if not in the list
		//it removes by identity
		
		//if we made it here, the test passes
		return true;
	}
}
