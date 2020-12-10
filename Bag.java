import java.util.*;
import java.io.*;


public class Bag{
    public String color;
    public ArrayList<Bag> bags;
    public ArrayList<Integer> counts;
    public Boolean hasGold = null;
       

    public Bag(String color){
	this.color = color;
	bags = new ArrayList<Bag>();
	counts = new ArrayList<Integer>();
	
    }

    
    public boolean equals(String color){
	return this.color.equals(color);
    }
    public boolean equals(Bag b){
	return this.equals(b.color);
    }
    public boolean addBag(Bag b, int count){
	bags.add(b);
	counts.add(count);
	return true;
    }
    public boolean find(String c){
	if (color.equals(c)) return true;
	if (bags.size() == 0) return false;
	boolean temp = false;
	for (Bag b: bags){
	    temp = temp || b.find(c);
	}
	return temp;
	
    }
    public String toString(){
	return color;
    }

    public static ArrayList<String[]> parseLine(String line){
	//System.out.println(line);
	ArrayList<String[]> split = new ArrayList<String[]>();
	String[] temp = line.split(" bags contain ", 5);
	if (temp[1].equals("no other bags.")){
	    split.add(temp);
	    return split;
	}

	String[] temp2 = temp[1].split(", ");	
	String[] parent = {temp[0]};
	split.add(parent);

	for (String curr: temp2){
	    String[] row = curr.split(" ");
	    String[] row2 = { row[0], row[1] + " " + row[2] };
	    split.add(row2);
	}
	
	return split;
    }
    public static ArrayList<String> readInLines(String fileName){
	ArrayList<String> lines = new ArrayList<String>();	
	try {
	    Scanner in = new Scanner(new File(fileName));
	    while (in.hasNextLine()) {
		lines.add(in.nextLine());
	    }
	    //System.out.println(lines);
	} catch (Exception E) { System.out.println(E); }
	return lines;
    }
    public static int contains(ArrayList<Bag> bags, String b){
	for (int i = 0;i < bags.size(); i++){
	    if (bags.get(i).equals(b)) return i;
	}
	return -1;
    }
    public static void main(String[] args){
	ArrayList<String> lines = readInLines("inputDay7.txt");
	int i = 0;
	ArrayList<Bag> bags = new ArrayList<Bag>();
	while (i < bags.size()){
	    //System.out.println(lines.get(i));
	    ArrayList<String[]> curr = parseLine(lines.get(i));
	    Bag b;
	    //System.out.println(bags);
	    if (contains(bags, curr.get(0)[0]) == -1){
		b = new Bag(curr.get(0)[0]);
		if (b.color.equals("shiny gold")) b.hasGold = false;
		bags.add(b);
	    }
	    else {
		b = bags.get(contains(bags,curr.get(0)[0]));
	    }
	    for (int j = 1; j < curr.size(); j++){
		int pos = contains(bags, curr.get(j)[1]);
		Bag toAdd;
		if (pos == -1){
		     toAdd = new Bag(curr.get(j)[1]);
		     if (curr.get(j)[1].equals("shiny gold"))
			 System.out.println(b);
			 b.hasGold = true;
		}
		else {
		    toAdd = bags.get(pos);
		    //System.out.println(toAdd.color);
		    if (toAdd.color.equals("shiny gold") && toAdd.hasGold != null){
			if (toAdd.hasGold == true){
			    System.out.println(b);
			    b.hasGold = true;
			}
		    }
		}
		b.addBag(toAdd, Integer.valueOf(curr.get(j)[0]));
	    }
	    i++;	
	}
	int count = 0;
	int count2 = 0;
	for (Bag b: bags){
	    //System.out.println("****************" + b.color);
	    //if (b.hasGold == null && !b.color.equals("shiny gold"))
	    //	b.hasGold = b.find("shiny gold");
	    // else if (b.color.equals("shiny gold")) b.hasGold = false;
	    //count += b.hasGold ? 1 : 0;
	    if (b.hasGold != null && b.hasGold) {
		count++;
		System.out.println(count);
		//System.out.println(b.color);
		//System.out.println(b.bags);
	    }
	    if (b.find("shiny gold")) count2++;
	}
    
	System.out.println(count2);
	
	
    
    }



    
}
	
