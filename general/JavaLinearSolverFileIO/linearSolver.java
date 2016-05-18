package linearSolverFiles;

import java.io.*;

public class linearSolver {
	
	public static String writeSolutions(float[][]matrix, int dimension, String stringOfSols){ // printing out the values for each variable
		for (int i = 0; i< dimension; i++){
			stringOfSols += ("x" + (i+1) + " = " + Math.round(matrix[i][dimension]*1000)/1000.0d) + System.lineSeparator();}
		return stringOfSols;
	}
	
	public static void rowSwap(float[][] matrix, int row1, int row2, int dimension){ // swapping two rows of the matrix
		float temp;
		for (int i = 0; i <= dimension; i++){
		 temp = matrix[row1][i];
		 matrix[row1][i] = matrix[row2][i];
		 matrix[row2][i] = temp;}
	}

	public static String checkPivot(float[][] matrix, int column, int dimension, String stringOfSols){ // checks to make sure pivot is non-zero, if it is zero: find a row to swap with
		if (matrix[column][column] != 0){
			return stringOfSols;
		}
		for (int i = column+1; i < dimension; i++){
			if (matrix[i][column] != 0){
				rowSwap(matrix, column, i, dimension);
				stringOfSols += ("Swapping rows " + (column+1) + " and " + (i+1) + " will give us:" + System.lineSeparator() + System.lineSeparator()); 
			stringOfSols = writeMatrix(matrix, dimension, stringOfSols);
			return stringOfSols;}}
		stringOfSols += ("no unique solution"); // if we made it this far, we couldn't find a non-zero row to swap with so there is no solution
		System.exit(0);
		return stringOfSols;
	}

	public static String divideRow(float[][] matrix, int row, int dimension, String stringOfSols){ // divide every row by the coefficient
		float divideValue = matrix[row][row]; // coefficient to divide by
		if (divideValue == 1) { // don't need to divide out the row if the pivot is already 1
			return stringOfSols;
		}
		stringOfSols += ("Dividing row " + (row+1) + " by " + Math.round(divideValue*1000)/1000.0d + " will give us:" + System.lineSeparator() + System.lineSeparator());
		for (int i = row; i <= dimension; i++){
			matrix[row][i] /= divideValue;}
		stringOfSols = writeMatrix(matrix, dimension, stringOfSols);
		return stringOfSols;
	}

	public static String zeroOutValuesAboveAndBelowThePivot(float[][] matrix, int column, int dimension, String stringOfSols){ // zero-ing out the values above and below the pivot 
		float zeroValue; // the coefficient that we want to 0 out
		for (int i = 0; i <dimension; i++){
		if (column == i){ // if we are in the same row as the pivot, skip (because we don't want to zero out the pivot)
			continue;}
		zeroValue = matrix[i][column];
		stringOfSols += ("Replacing row" + (i+1) + " with row" + (i+1) + " - " + Math.round(zeroValue*1000)/1000.0d + "*" + "row" + (column+1) + " to give us:" + System.lineSeparator() + System.lineSeparator());
		for (int j = 0; j <= dimension; j++){
			matrix[i][j] -= zeroValue*matrix[column][j];}
		stringOfSols = writeMatrix(matrix, dimension, stringOfSols);
			} // doing operations on the whole row
	return stringOfSols;
	}

	
	
	
	public static String solveColumn(float[][] matrix, int column, int dimension, String stringOfSols){ // do all necessary row operations to complete all steps on one column
		stringOfSols += ("Working on column " + (column+1) + " now" + System.lineSeparator() + System.lineSeparator());
		stringOfSols = checkPivot(matrix, column, dimension, stringOfSols); // make sure the entry where we want the pivot is non-zero
		stringOfSols = divideRow(matrix, column, dimension, stringOfSols); // divide the row by the value we want to make a pivot
		stringOfSols = zeroOutValuesAboveAndBelowThePivot(matrix, column, dimension, stringOfSols); // zero'ing out everything about and below the pivot
	return stringOfSols;
	}
	
	public static String RREF(float[][] matrix, int dimension, String stringOfSols){
		for (int i = 0; i < dimension; i++){
			stringOfSols = solveColumn(matrix, i, dimension, stringOfSols);}
		return stringOfSols;
	}
	
	
	public static String writeMatrix(float[][] matrix, int dimension, String strOfSols){
		 for (int i = 0; i < dimension; i++){
			 for (int j = 0; j < dimension+1; j++){
				 strOfSols += String.valueOf(Math.round(matrix[i][j]*1000)/1000.0d) + "\t";
				
			 }
			 strOfSols +=  System.lineSeparator() + System.lineSeparator();
		 }
		 return strOfSols;
	}

	public static void main(String[] args) {
		
		 int dimension = 0;
		 String strOfSols = "";
		    float matrix[][] = null;
			try{
			//	 int dimension;
				 int row = 0;
				 String[] splitInp;
				 File myFile = new File("input.txt");
				 FileReader fileReader = new FileReader(myFile);
				 BufferedReader reader = new BufferedReader(fileReader);
				 String line = null;
				 line = reader.readLine();
				 dimension = Integer.valueOf(line);
				 matrix = new float[dimension][dimension+1];
				 while ((line = reader.readLine()) != null){
				  splitInp = line.split("\t");
				  for (int col = 0; col < dimension+1; col++){
					matrix[row][col] = Float.valueOf(splitInp[col]); 
				  }
				  row++;
				 } // while
				 reader.close();
				 strOfSols += "You entered: " + System.lineSeparator() + System.lineSeparator();
				 strOfSols = writeMatrix(matrix, dimension, strOfSols);
				 strOfSols += "Now to convert this to RREF" + System.lineSeparator() + System.lineSeparator();
				 strOfSols = RREF(matrix, dimension, strOfSols);
				 reader.close();
				 strOfSols += ("The matrix is now in RREF. Picking off the right-most entries to give us the solution for each variable gives us:" + System.lineSeparator() + System.lineSeparator());
				 strOfSols = writeSolutions(matrix, dimension, strOfSols); 
			     }
				 catch(IOException ex){
				  ex.printStackTrace(); 
				 }

			try{
				 FileWriter writer = new FileWriter("output.txt");
				 writer.write(strOfSols);
				 writer.close();
				   }
				catch(IOException ex){
				 ex.printStackTrace();
				   }
		
	}

}
