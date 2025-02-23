function M66 = findelemm66(ELEM, varargin)
%FINDELEMM66 numerically finds the 6x6 transfer matrix of an element
%  M66=FINDELEMM66(ELEM, METHODNAME)
%     ELEM          - the element data structure
%     METHODNAME    - name of the pass-method function
%                   (default:  ELEM.PassMethod)
%
%  M66=FINDELEMM66(ELEM, METHODNAME, ORBITIN)  (Deprecated syntax)
%  M66=FINDELEMM66(...,'orbit',ORBITIN)
%     ORBITIN       - 6-by-1 phase space coordinates at the entrance
%                   (default: zeros(6,1))
%
%  M66=FINDELEMM66(...,'Energy',ENERGY)
%     Use ENERGY and ignore the 'Energy' field of elements
%
%  M66=FINDELEMM66(...,'Particle',PARTICLE)
%     Use PARTICLE (default is relativistic)
% 
% See also FINDELEMM44

[XYStep,varargs]=getoption(varargin,'XYStep');
[R0,varargs]=getoption(varargs,'orbit',zeros(6,1));
[energy,varargs]=getoption(varargs,'Energy',0.0);
[particle,varargs]=getoption(varargs,'Particle',[]);
[MethodName,R0]=getargs(varargs,ELEM.PassMethod,R0);

% Build a diagonal matrix of initial conditions
%scaling=2*XYStep*[1 0.1 1 0.1 1 1];
scaling=XYStep*[1 1 1 1 1 1];
D6 = 0.5*diag(scaling);
% Add to the orbit_in
RIN = R0 + [D6, -D6];
% Propagate through the element
ROUT=elempass(ELEM,RIN,'PassMethod',MethodName,'Energy',energy,'Particle',particle);
% Calculate numerical derivative
M66 = (ROUT(:,1:6)-ROUT(:,7:12))./scaling;
