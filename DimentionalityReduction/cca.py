
"""
Canonical Correlation Analysis 

originally by Magnus Borga, Linköpings universitet in Matlab
modified to Kernel CCA by Taylor Berg-Kirkpatrick
ported to Python by Siamak Faridani

July 2010
UC Berkeley

TODO: Make it more like python not Matlab :) 

"""
"""
% CCA calculate canonical correlations
%
% [Wx Wy r] = cca(X,Y) where Wx and Wy contains the canonical correlation
% vectors as columns and r is a vector with corresponding canonical
% correlations. The correlations are sorted in descending order. X and Y
% are matrices where each column is a sample. Hence, X and Y must have
% the same number of columns.
%
% Example: If X is M*K and Y is N*K there are L=MIN(M,N) solutions. Wx is
% then M*L, Wy is N*L and r is L*1.
%
%
% © 2000 Magnus Borga, Linköpings universitet
"""

function [Wx, Wy, invWx, invWy, P] = kernel_cca(X,Y, reg)


n = size(X,2);
sx = size(X,1);
sy = size(Y,1);
L = min(sx,sy);
Kxx = X'*X;
Kyy = Y'*Y;
invKxx = inv(Kxx + reg*eye(n));
invKyy = inv(Kyy + reg*eye(n));


[Alpha,r] = eig(invKxx*Kyy*invKyy*Kxx);
r = sqrt(r);      % Canonical correlations
Beta = invKyy*Kxx*Alpha;

Wx = X*Alpha;
Wy = Y*Beta;     % Basis in Y

% --- Sort correlations ---

Vx = fliplr(Wx); % reverse order of eigenvectors
Vy = fliplr(Wy); % reverse order of eigenvectors
r = flipud(diag(r));	% extract eigenvalues anr reverse their orrer
[r,I]= sort(r);	% sort reversed eigenvalues in ascending order
r = flipud(r);		% restore sorted eigenvalues into descending order
for j = 1:length(I)
  Wx(:,j) = Vx(:,I(j));  % sort reversed eigenvectors in ascending order
  Wy(:,j) = Vy(:,I(j));  % sort reversed eigenvectors in ascending order
end
Wx = fliplr(Wx);	% restore sorted eigenvectors into descending order
Wy = fliplr(Wy);	% restore sorted eigenvectors into descending order

Wx=Wx(:,1:L);
Wy=Wy(:,1:L);
r = r(1:L);

Wx = Wx ./repmat(sqrt(diag(Wx'*X*X'*Wx)'),sx,1);
Wy = Wy ./repmat(sqrt(diag(Wy'*Y*Y'*Wy)'),sy,1);

P = diag(diag(Wx'*X*Y'*Wy));

% Wx = Wx*sqrt(P);
% Wy = Wy*sqrt(P);

invWx = (X*X'*Wx)';
invWy = (Y*Y'*Wy)';

% invWx = ((X*X')*Wx*sqrt(P))';
% invWy = ((Y*Y')*Wy*sqrt(P))';
