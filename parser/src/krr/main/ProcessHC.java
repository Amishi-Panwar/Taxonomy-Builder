/*
 * A program to convert Horn Clause program to XML format.
 * published by:
 *    Department of Computer Science and Engineering,
 *    Indian Institute of Technology Madras,
 *    Chennai-36, India.
 *
 * Copyright 2012 Indian Institute of Technology Madras.  All Rights Reserved.
 * DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
 *
 * This code is part of the course assignment;
 * you can redistribute it and/or modify it as long as this header is retained.
 *
 * This code is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE.
 */
/* Revision History:
 * Date        Author                Description/Change
 * 2012-03-06  S.Baskaran            First release
 * 2022-04-02  S.Baskaran            Using simpleTokens() to reduce XML clutter.
 */

package krr.main;

import org.antlr.runtime.ANTLRFileStream;
import org.antlr.runtime.CharStream;
import org.antlr.runtime.CommonTokenStream;
import in.ac.iitm.cse.parser.hc.HCLexer;
import in.ac.iitm.cse.parser.hc.HCParser;
import in.ac.iitm.cse.tree.AST;
import in.ac.iitm.cse.tree.ASTAdaptor;
import in.ac.iitm.cse.tree.ASTPrinter;

/**
 *
 * @author baskaran
 */
public class ProcessHC extends Process {

    private ProcessHC() { super(); }

    static private ProcessHC instance=null;
    static public ProcessHC getInstance() {
        if (instance == null) {
            instance = new ProcessHC();
        }
        return instance;
    }

    static boolean debug=false;
    public void debug() { debug=true; }

    public void run(String infile) {
        try {
            CharStream input = new ANTLRFileStream(infile);
            HCLexer lex = new HCLexer(input);

            CommonTokenStream tokens = new CommonTokenStream(lex);
            HCParser parser = new HCParser(tokens);

            ASTAdaptor adaptor = new ASTAdaptor();
            parser.setTreeAdaptor(adaptor);

            AST t = (AST) parser.cunit().getTree();

            //if (debug) {
            //    System.out.print("AST:\n");
            //    System.out.println(t.toStringTree());
            //}

            ASTPrinter.print(t,parser.getTokenNames(),lex.simpleTokens(),lex.textAttribute(), debug);
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }

}
