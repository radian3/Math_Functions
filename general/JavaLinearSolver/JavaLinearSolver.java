package linearSolver;

import java.io.*;

public class main {
	
	
	public static void printSolutions(float[][]matrix, int dimension){ // printing out the values for each variable
		for (int i = 0; i< dimension; i++){
			System.out.println("x" + (i+1) + " = " + Math.round(matrix[i][dimension]*1000)/1000.0d);}
	}
	
	public static void rowSwap(float[][] matrix, int row1, int row2, int dimension){ // swapping two rows of the matrix
		float temp;
		for (int i = 0; i <= dimension; i++){
		 temp = matrix[row1][i];
		 matrix[row1][i] = matrix[row2][i];
		 matrix[row2][i] = temp;}
	}

	public static void checkPivot(float[][] matrix, int column, int dimension){ // checks to make sure pivot is non-zero, if it is zero: find a row to swap with
		if (matrix[column][column] != 0){
			return;
		}
		for (int i = column+1; i < dimension; i++){
			if (matrix[i][column] != 0){
				rowSwap(matrix, column, i, dimension);
			System.out.print("Swapping rows " + (column+1) + " and " + (i+1) + " will give us:\n\n"); 
			printMatrix(matrix, dimension);
			return;}}
		System.out.print("no unique solution"); // if we made it this far, we couldn't find a non-zero row to swap with so there is no solution
		System.exit(0);
	}

	public static void divideRow(float[][] matrix, int row, int dimension){ // divide every row by the coefficient
		float divideValue = matrix[row][row]; // coefficient to divide by
		if (divideValue == 1) { // don't need to divide out the row if the pivot is already 1
			return;
		}
	System.out.print("Dividing row " + (row+1) + " by " + Math.round(divideValue*1000)/1000.0d + " will give us:\n\n");
		for (int i = row; i <= dimension; i++){
			matrix[row][i] /= divideValue;}
		printMatrix(matrix, dimension);	
	}

	public static void zeroOutValuesAboveAndBelowThePivot(float[][] matrix, int column, int dimension){ // zero-ing out the values above and below the pivot 
		float zeroValue; // the coefficient that we want to 0 out
		for (int i = 0; i <dimension; i++){
		if (column == i){ // if we are in the same row as the pivot, skip (because we don't want to zero out the pivot)
			continue;}
		zeroValue = matrix[i][column];
		System.out.print("Replacing row" + (i+1) + " with row" + (i+1) + " - " + Math.round(zeroValue*1000)/1000.0d + "*" + "row" + (column+1) + " to give us:\n\n");
		for (int j = 0; j <= dimension; j++){
			matrix[i][j] -= zeroValue*matrix[column][j];}
		printMatrix(matrix, dimension);
			} // doing operations on the whole row
	}

	
	
	
	public static void solveColumn(float[][] matrix, int column, int dimension){ // do all necessary row operations to complete all steps on one column
		System.out.print("Working on column " + (column+1) + " now\n\n");
		checkPivot(matrix, column, dimension); // make sure the entry where we want the pivot is non-zero
		divideRow(matrix, column, dimension); // divide the row by the value we want to make a pivot
		zeroOutValuesAboveAndBelowThePivot(matrix, column, dimension); // zero'ing out everything about and below the pivot
	}
	
	public static void RREF(float[][] matrix, int dimension){
		for (int i = 0; i < dimension; i++){
			solveColumn(matrix, i, dimension);}
	}
	
	
	public static void printMatrix(float[][] matrix, int dimension){
		 for (int i = 0; i < dimension; i++){
			 for (int j = 0; j < dimension+1; j++){
				 System.out.print(Math.round(matrix[i][j]*1000)/1000.0d + "\t");
				
			 }
			 System.out.print("\n\n");
		 }
	}
	

	
	public static void main(String[] args){
	    int dimension = 0;
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
			 System.out.println("You entered: \n");
			 printMatrix(matrix, dimension);
			 System.out.println("Now to convert this to RREF\n");
			 RREF(matrix, dimension);
			 reader.close();
			 System.out.println("The matrix is now in RREF. Picking off the right-most entries to give us the solution for each variable gives us:\n");
			 printSolutions(matrix, dimension); 
		     }
			 catch(IOException ex){
			  ex.printStackTrace(); 
			 }
		
		
	    
		
		} // main
	
}
