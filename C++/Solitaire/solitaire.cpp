#include <iostream>
#include <iomanip>
#include <random>
#include <vector>
#include <string>
using namespace std;

void printDeck(std::vector<std::vector<std::string> > input);
int myrandom (int i) { return std::rand()%i;}

int main()
{
  srand(time(0));
  time_t begin = time(0);

  int nGames = 1000000;
  double nWins = 0;

  std::string ace      = "Ace";
  std::string two      = "2";
  std::string three    = "3";
  std::string four     = "4";
  std::string five     = "5";
  std::string six      = "6";
  std::string seven    = "7";
  std::string eight    = "8";
  std::string nine     = "9";
  std::string ten      = "10";
  std::string jack     = "Jack";
  std::string queen    = "Queen";
  std::string king     = "King";
  std::string hearts   = "Hearts";
  std::string spades   = "Spades";
  std::string diamonds = "Diamonds";
  std::string clubs    = "Clubs";

  std::vector<std::string> numberList;
  std::vector<std::string> suitList;
  std::vector<std::vector<std::string> > cardList;

  numberList.push_back(ace);     
  numberList.push_back(two);
  numberList.push_back(three);   
  numberList.push_back(four); 
  numberList.push_back(five);    
  numberList.push_back(six);     
  numberList.push_back(seven);   
  numberList.push_back(eight);   
  numberList.push_back(nine);    
  numberList.push_back(ten);     
  numberList.push_back(jack);    
  numberList.push_back(queen);   
  numberList.push_back(king);    
  suitList.push_back(hearts);  
  suitList.push_back(spades);
  suitList.push_back(diamonds);
  suitList.push_back(clubs);

  std::vector<std::string> temp;
  for(int num = 0 ; num < numberList.size() ; num++){
    for(int suit = 0 ; suit < suitList.size() ; suit++){
      temp.push_back(numberList.at(num));
      temp.push_back(suitList.at(suit));
      cardList.push_back(temp);
      temp.clear();
    }
  }


  std::vector<std::vector<std::string> > deck;
  //THIS PART NEEDS TO BE DONE MANY TIMES
  for(int game = 0 ; game < nGames ; game++){
    if((game+1) % 10000 == 0) {cout << "Game: " << game+1 << endl;}
    deck = cardList;
    std::random_shuffle(deck.begin(),deck.end(),myrandom);
    //printDeck(deck);
    bool done = false;
    while(!done){
      bool none = true;
      for(int i = 0 ; i < deck.size()-3 ; i++){
	int j = i + 3;
	if(deck.size() < 4) break;
	if(deck.at(i).at(0) == deck.at(j).at(0)){
	  //cout << deck.at(i).at(0) << " of " << deck.at(i).at(1) << " and " << deck.at(j).at(0) << " of " << deck.at(i).at(1) << endl;
	  deck.erase(deck.begin() + i,deck.begin() + j + 1);
	  none = false;
	  break;
	} else if(deck.at(i).at(1) == deck.at(j).at(1)){
	  //cout << deck.at(i).at(0) << " of " << deck.at(i).at(1) << " and " << deck.at(j).at(0) << " of " << deck.at(i).at(1) << endl;
          deck.erase(deck.begin() + i + 1,deck.begin() + j);
          none = false;
	  break;
	}
      }
      if(none == true){ done = true;}
    }
    if(deck.size() == 0) {nWins = nWins + 1;}
    
  }

  time_t end = time(0);
  cout << "Number of wins: " << nWins << "/" << nGames << "          Time: " << end-begin << " s" << endl;

  return 0;

}


void printDeck(std::vector<std::vector<std::string> > input){
  cout << "PRINTING DECK!!! There are " << input.size() << " cards left" << endl;
  for(int i = 0 ; i < input.size() ; i++){
    cout << i+1 << ": " << input.at(i).at(0) + " of " + input.at(i).at(1) << endl;
  }
}
