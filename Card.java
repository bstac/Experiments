
public class Card implements Comparable<Card>
{
	private Rank rank;
	private Suit suit;
	
	/**
	 * basic card constructor
	 *  @author Brandon Stack
	 * @param _rank
	 * @param _suit
	 */
	public Card(Rank _rank, Suit _suit)
	{
		rank = _rank;
		suit = _suit;
	}
	/**
	 * copy constructor
	 *  @author Brandon Stack
	 * @param card
	 */
	public Card(Card card)
	{
		rank = card.getRank();
		suit = card.getSuit();
	}
	/**
	 * return the rank property
	 *  @author Brandon Stack
	 * @return
	 */
	public Rank getRank()
	{
		return rank;
	}

	/**
	 * get the suit
	 *  @author Brandon Stack
	 * @return
	 */
	public Suit getSuit()
	{
		return suit;
	}
	/* (non-Javadoc)
	 * @see java.lang.Object#toString()
	 */
	public String toString()
	{
		return "Card - " + rank.toString() + 
				" : " + suit.toString();
	}
	/* (non-Javadoc)
	 * @see java.lang.Comparable#compareTo(java.lang.Object)
	 */
	@Override
	public int compareTo(Card c) 
	{
		return this.getRank().ordinal() - c.getRank().ordinal();
	}
	/* (non-Javadoc)
	 * @see java.lang.Object#equals(java.lang.Object)
	 */
	@Override 
	public boolean equals(Object o)
	{
		if(!(o instanceof Card)){return false;}
		Card c = (Card)o;
		return this.rank == c.getRank() && this.suit == c.getSuit();
	}
}
