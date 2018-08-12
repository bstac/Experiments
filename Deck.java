import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;


public class Deck 
{
	private ArrayList<Card> cards;
	private Random random;
	
	/**
	 * default constructor
	 *  @author Brandon Stack
	 */
	public Deck()
	{
		//default constructor
		cards = new ArrayList<Card>();
		random = new Random(System.currentTimeMillis());
	}
	
	/**
	 * Array list copy constructor
	 *  @author Brandon Stack
	 * @param _cards
	 */
	public Deck(ArrayList<Card> _cards)
	{
		cards = new ArrayList<Card>();
		random = new Random(System.currentTimeMillis());
		for(Card card : _cards)
		{
			 cards.add(new Card(card)); //use copy constructor
		}
	}
	
	/**
	 * actual copy constructor, deep.
	 *  @author Brandon Stack
	 * @param deck
	 */
	public Deck(Deck deck)
	{
		cards = new ArrayList<Card>();
		random = new Random(System.currentTimeMillis());
		for(Card card : deck.toList())
		{
			 cards.add(new Card(card)); //use copy constructor
		}
	}
	
	
	/**
	 * add a card. adds a reference, not a copy. prevents duplicates.
	 *  @author Brandon Stack
	 * @param card
	 */
	public void addCard(Card card)
	{
		if(!cards.contains(card))//unique, but has definite order
		{
			cards.add(card);
		}
	}
	/**
	 * remove a card by id or value.
	 *  @author Brandon Stack
	 * @param card
	 */
	public void removeCard(Card card)
	{
		cards.remove(card);	
	}
	/**
	 * Shuffle (by swapping each card). tested to have a good-enough distribution.
	 *  @author Brandon Stack
	 */
	public void shuffle()
	{
		for(int i=0; i<cards.size();i++)
		{//one random swap per
			int a = random.nextInt(cards.size());
			Collections.swap(cards, i, a);//no need to re-create the wheel
		}
	}
	/**
	 * draw from the top. Cards lay face down on a table, so this acts as a stack.
	 *  @author Brandon Stack
	 * @return
	 */
	public Card draw()
	{//for this, I am imagining a deck is a stack
		//add goes one on top of the previous, 
		//but you then draw from the last card to be added
		return cards.remove(cards.size()-1);//as it turns out, the minus 1 is important
	}
	/**
	 * to list function, uses arrayList
	 *  @author Brandon Stack
	 * @return
	 */
	public List<Card> toList()
	{
		List<Card> cardArray = new ArrayList<Card>();
		for(Card card : cards)
		{
			cardArray.add(new Card(card)); //use copy constructor
		}
		return cardArray;
	}
}
