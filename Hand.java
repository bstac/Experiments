
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;


public class Hand 
{
	private ArrayList<Card> cards;
	
	/**
	 * default constructor
	 *  @author Brandon Stack
	 */
	public Hand()
	{
		//default constructor
		cards = new ArrayList<Card>();
	}
	
	/**
	 * copy from arrayList
	 *  @author Brandon Stack
	 * @param _cards
	 */
	public Hand(ArrayList<Card> _cards)
	{
		cards = new ArrayList<Card>();
		for(Card card : _cards)
		{
			 cards.add(new Card(card)); //use copy constructor
		}
	}

	/**
	 * copy from Hand.
	 *  @author Brandon Stack
	 * @param hand
	 */
	public Hand(Hand hand)
	{
		cards = new ArrayList<Card>();
		for(Card card : hand.toList())
		{
			 cards.add(new Card(card)); //use copy constructor
		}
	}
	
	/**
	 * add a card. Prevents duplicates. Adds by reference/ID (meaning does not copy).
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
	 * Sort the hand using Comparable Interface.
	 *  @author Brandon Stack
	 */
	public void sortHand()
	{
		Collections.sort(cards);
	}
	
	//Remove() and Contains() are ambiguous with respect to Identity v.s. Value
	//Some games are played with multiple decks, 
	//and so you can have more than one card of the same suit, rank
	/**
	 * remove a card. Removes by value.
	 *  @author Brandon Stack
	 * @param card
	 */
	public void removeCard(Card card)
	{
		cards.remove(card);
	}
	/**
	 * Tests if a cards value is in the list.
	 * @author Brandon Stack
	 * @param card
	 * @return
	 */
	public boolean contains(Card card)
	{
		return cards.contains(card);
	}
	
	/**
	 * To List. Usees arrayList.
	 *  @author Brandon Stack
	 * @return
	 */
	public List<Card> toList()
	{
		//we don't want to give the user a our private data
		//but we can give them a copy of everything
		List<Card> cardArray = new ArrayList<Card>();
		for(Card card : cards)
		{
			cardArray.add(new Card(card)); //use copy constructor
		}
		return cardArray;
	}
}

