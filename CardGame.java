import java.util.ArrayList;
import java.util.List;


public abstract class CardGame 
{
	protected String Title;
	protected boolean Continue = true; //for exits from player input
	protected Deck theDeck; //one and only deck, for all games
	protected Hand playerHand;
	protected Hand computerHand;
	
	//all games are going to be two players
	//one human, one computer
	//the computer goes first (for my sake)
	
	protected List<Rank> ranks; //not all games have all of the designated ranks
	protected List<Suit> suits; //suits, will most likely be the four, but just in case
	
	/**
	 * Need to set the rank list, which will be used in eck creation.
	 */
	protected abstract void SetRanks(); //create the deck before initial deal
	/**
	 * need to set the suit list, which will be used in deck creation.
	 */
	protected abstract void SetSuits(); //create the deck before initial deal
	
	/**
	 * display a game menu and handle any initial configuration of a game
	 */
	protected abstract void GameMenu(); 
	//sub menu for this specific game (other menus maybe required in subclasses)
	/**
	 * A sedtup function for all pre game attributes
	 */
	protected abstract void StartGame();//setup function, initial deal and such
	/**
	 * the user gets turn, and this is where the logic goes for that.
	 */
	protected abstract void PlayerTurn();
	/**
	 * computer turn.
	 */
	protected abstract void ComputerTurn();
	/**
	 * an extra space for decisions, reports, etc... between rounds
	 */
	protected abstract void DecisionTurn();
	/**
	 * a function that tests if the game has ended.
	 * returns "should continue?", not "are we there yet?"
	 * or rather, confirms in the positive, not the negative.
	 * @return
	 */
	protected abstract boolean TestGameEndCondition();
	//returns "should continue?", not "are we there yet?"
	/**
	 * The game needs to be scored. Who won? was there a tie?
	 */
	protected abstract void ScoreGame();
	/**
	 * Reset, necessary if you would like persistent objects in Games list.
	 */
	protected abstract void Reset();
	
	//sometimes rank is more than just an order/lattice
	//sometimes defined values are wanted, but they depend on the game
	//black jack is going to present a particular problem here
	//so function rather than map/hash/dictionary
	/**
	 * For mapping ranks given game state or other 'funky' situations.
	 * Ex. in black jack, an ace can switch from 11 to 2, when needed.
	 * @param rank
	 * @return
	 */
	protected abstract int ScoreRank(Rank rank);
	
	/**
	 * Create Deck. All Games share this sequence.
	 * Instantiates dependents and then loops through the rank and suit lists
	 * to create a complete deck, and then shuffles.
	 */
	protected void CreateDeck()
	{//create the deck before initial deal
		playerHand = new Hand();
		computerHand = new Hand();
		
		theDeck = new Deck();
		ranks = new ArrayList<Rank>();
		suits = new ArrayList<Suit>();
		SetSuits();
		SetRanks();
		for(Suit s : suits)
		{
			for(Rank r : ranks)
			{
				theDeck.addCard(new Card(r,s));
			}
		}
		theDeck.shuffle();
	}
	/**
	 * Persistent game flow for all CardGames.
	 * Display Menu, Create Deck, Start Game.
	 * Then loop. Computer turn (computer is always first), Player turn, and decision round
	 * until the End condition is met, or user exits.
	 * Then the game is scored and the game is reset.
	 */
	public void PlayGame()
	{//main game loop
		GameMenu();//will set options as needed
		CreateDeck();
		StartGame();
		while(TestGameEndCondition() && Continue)
		{
			ComputerTurn();
			PlayerTurn();
			DecisionTurn();
		}
		ScoreGame();
		Reset();
	}
	
	/**
	 * the title to be set in the base class constructor
	 * helps for things like print a common phrase.
	 * @return
	 */
	public String GetTitle()
	{
		return Title;
	}
}
